def answer(l):
	mult = [-1 for a in range(len(l))]	
	count = 0
	for i in  range(len(l)):
		for j in range(i+1, len(l)):
			if l[j]%l[i] == 0:
				if mult[j] == -1:
					mult[j] = 0
					for k in range(j+1, len(l)):
						if l[k]%l[j] == 0:
							mult[j] += 1
					
				count += mult[j]
		
	return count
	
l = [6,2, 3, 12, 24] 
print answer(l)
						
			