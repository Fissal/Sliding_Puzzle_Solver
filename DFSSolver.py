from Parameters import *
from PuzzleState import *
# import pylab
import sys

class DFSSolver:
    @staticmethod
    def solve(initialState):
        solution = DFSSolver.dfs(initialState)
        if solution is None:
            return None
        arr = [solution]
        while solution.parent is not None:
            solution = solution.parent
            arr.append(solution)
        print(len(arr))
        reversedArr = arr[::-1]
        return reversedArr

    @staticmethod
    def dfs(initialState):
        frontier = [initialState]
        initialState.parent = None
        initialState.level = 0
        visited = {initialState}
        totalVisited = 0
        L1 = []
        L2 = []
        L3 = []
        while frontier:
            totalVisited = totalVisited + 1
            L1.append(totalVisited)
            selected = frontier[-1]
            if DEBUG:
                #print('level: ' + str(selected.level) + ',totalVisited: ' + str(totalVisited) + ',len(frontier): ' + str(len(frontier)))
                sys.stdout.flush()
                L2.append(int(selected.level))
                L3.append(int(len(frontier)))
            del frontier[-1]
            if selected.isSolved():
                #pylab.plot(L1,L3) #Total Visited vs Frontier !
                #pylab.plot(L1,L2) #Total Visited vs Selected Level !
                #pylab.xlabel('Total Visited')
                #pylab.ylabel('Selected Level')
                #pylab.ylabel('Frontier')
                #pylab.show()
                print('success')
                print('Level: ' + str(selected.level))
                print('Total visited: ' + str(totalVisited))
                return selected
            branches = selected.getBranchPuzzleStates()
            for b in branches:
                if b not in visited:
                    visited.add(b)
                    b.parent = selected
                    b.level = selected.level + 1
                    frontier.append(b)
        print('no solution. :(')
        print('Total visited: ' + str(totalVisited))


