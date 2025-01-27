from BFS_tracked import BFS
from DFS_tracked import DFS
from pyamaze import maze,agent,COLOR,textLabel
from timeit import timeit

m=maze(20,30)

m.CreateMaze(loopPercent=50)

searchPath,dfsPath,fwdDFSPath=DFS(m)
bSearch,bfsPath,fwdBFSPath=BFS(m)

textLabel(m,'DFS Path Length',len(fwdDFSPath)+1)
textLabel(m,'BFS Path Length',len(fwdBFSPath)+1)
textLabel(m,'DFS Search Length',len(searchPath)+1)
textLabel(m,'BFS Search Length',len(bSearch)+1)

a=agent(m,footprints=True,color=COLOR.cyan,shape='arrow')
b=agent(m,footprints=True,color=COLOR.yellow)
m.tracePath({a:fwdBFSPath},delay=150)
m.tracePath({b:fwdDFSPath},delay=150)


t1=timeit(stmt='DFS(m)',number=1000,globals=globals())
t2=timeit(stmt='BFS(m)',number=1000,globals=globals())

textLabel(m,'DFS Time',t1)
textLabel(m,'BFS Time',t2)


m.run()
