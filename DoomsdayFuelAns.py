def lcmoflist(con):
    distinct = []
    for i in con:
        if i not in distinct:
            distinct.append(i)
    lcm = max(distinct)
    while any(lcm % x != 0 for x in distinct):
        lcm += 1
    return lcm


def transpose(sub):
    return map(list, zip(*sub))


def Minor(sub, i, j):
    return [row[:j] + row[j + 1:] for row in (sub[:i] + sub[i + 1:])]


def Deternminant(mat):
    # base case for 2x2 matrix
    if len(mat) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    determinant = 0
    for c in range(len(mat)):
        determinant += ((-1) ** c) * mat[0][c] * Deternminant(Minor(mat, 0, c))
    return determinant


def Inverse(mat):
    determinant = Deternminant(mat)

    if len(mat) == 2:
        return [[mat[1][1] / determinant, -1 * mat[0][1] / determinant],
                [-1 * mat[1][0] / determinant, mat[0][0] / determinant]]

    inverse = []
    for r in range(len(mat)):
        inverseRow = []
        for c in range(len(mat)):
            minor = Minor(mat, r, c)
            inverseRow.append(((-1) ** (r + c)) * Deternminant(minor))
        inverse.append(inverseRow)
    inverse = transpose(inverse)
    for r in range(len(inverse)):
        for c in range(len(inverse)):
            inverse[r][c] = inverse[r][c] / determinant
    return inverse


def answer(m):
    from fractions import Fraction
    trans = []
    trm = []
    i = 0
    for item in m:
        if all(el == 0 for el in item):
            trm.append(i)
        else:
            trans.append(i)
            s = sum(item)
            m[i][:] = [Fraction(x, s) for x in item]
        i += 1
    if not trans:
        ret = [1]
        for a in range(len(trm) - 1):
            ret.append(0)
        ret.append(1)
        return ret

    R = []
    Q = []
    for a in trans:
        R.append([m[a][b] for b in trm])
        Q.append([m[a][c] for c in trans])

    I = []
    j = 0
    for j in range(len(Q)):
        row = []
        for k in range(len(Q)):
            if j == k:
                row.append(1)
            else:
                row.append(0)
        I.append(row)
    IminusQ = []
    for i in range(len(I)):
        IminusQ.append([I[i][j] - Q[i][j] for j in range(len(I))])
    F = Inverse(IminusQ)
    FR = []
    for i in range(len(F)):
        FR.append([])
        for j in range(len(R[0])):
            FR[i].append(0)
            for k in range(len(R)):
                FR[i][j] += F[i][k] * R[k][j]

    lcmdenom = lcmoflist([a.denominator for a in FR[0]])
    ret = [a.numerator * lcmdenom / a.denominator for a in FR[0]]
    ret.append(lcmdenom)
    return ret