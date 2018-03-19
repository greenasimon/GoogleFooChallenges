def answer(maze):
	if len(maze)==0:
		return 0
	from Queue import Queue
	startnode = {'i':0, 'j':0, 'count':1, 'flag':0}
	trav = Queue()
	
	loop = startnode
	 # 4 - not to be repeated state
	while not trav.empty() or not(loop['i']==len(maze)-1 and loop['j'] == len(maze[0])-1):
		
		
		i = loop['i']
		j = loop['j']
		if maze[i][j]==-1:
			loop = trav.get()
			continue
		if maze[i][j] == 1:
			if loop['flag']==1:
				loop = trav.get()
				continue
			else:
				maze[i][j]=-1
				loop['flag']=1
		else:
			if (maze[i][j] == 2 and loop['flag']==0)or (maze[i][j]==3 and loop['flag']==1) or maze[i][j] == 4:
				loop = trav.get()
				continue
			else:
				if maze[i][j]==2 or maze[i][j]==3:
					maze[i][j] = 4
				else:
					if loop['flag']==0:
						maze[i][j]=2
					else: maze[i][j]=3
		childlist = [{'i':i+1, 'j':j}, {'i':i-1, 'j':j}, {'i':i, 'j':j+1,}, {'i':i, 'j': j-1}]
		
		for child in childlist:
			if (child['i']==len(maze) -1) and (child['j']==len(maze[0])-1):
				return loop['count']+1
			if (child['i']>=0 and child['i']<len(maze)) and (child['j']>=0 and child['j'] < len(maze[0])):
				childnode = {'i':child['i'], 'j':child['j'], 'count':loop['count']+1, 'flag':loop['flag']}
				trav.put(childnode)
				
		loop = trav.get()
	return loop['count']
	
maze = [[0,0,0,0,0],[0,0,0,0,0]]
print answer(maze)
                            

			
					
				
			
		