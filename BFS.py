from pyamaze import maze,agent,COLOR,textLabel
import timeit
def BFS(m):
    start=(m.rows,m.cols)
    frontier=[start]
    explored=[start]
    bfsPath={}
    while len(frontier)>0:
        currCell=frontier.pop(0)
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return fwdPath

if __name__=='__main__':
    m=maze(15,10)
    m.CreateMaze(loopPercent=40,theme='custom1')
    path=BFS(m)

    a=agent(m,footprints=True,filled=False,shape='arrow',color=COLOR.custom2)
    m.tracePath({a:path},delay=250)
    l=textLabel(m,'Length of Shortest Path',len(path)+1)

    t=timeit.timeit(stmt='BFS(m)',number=1000,globals=globals())
    textLabel(m,'BFS Time',t)

    m.run()
