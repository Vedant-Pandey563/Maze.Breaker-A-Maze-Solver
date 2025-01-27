from pyamaze import maze, agent, COLOR, textLabel
import timeit

def DFS(m):
    start = (m.rows, m.cols)
    explored = [start]
    frontier = [start]
    dfsPath = {}
    while len(frontier) > 0:
        currCell = frontier.pop()
        if currCell == (1, 1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                dfsPath[childCell] = currCell
    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return fwdPath

if __name__ == '__main__':
    m = maze(15, 10)
    m.CreateMaze(loopPercent=50)
    path = DFS(m)
    a = agent(m, footprints=True, filled=False, shape='arrow', color=COLOR.custom2)
    m.tracePath({a: path})

    textLabel(m, 'DFS Path Length', len(path) + 1)
 

    t= timeit.timeit(stmt='DFS(m)', number=1000, globals=globals())
    textLabel(m, 'DFS Time', t)

    m.run()
