import operator
import bisect
from Parameters import *
# import pylab
import sys

class AStarSolver:
    @staticmethod
    def solve(initialState):
        solution = AStarSolver.astar(initialState)
        if solution is None:
            return None
        arr = [solution]
        while solution.parent is not None:
            solution = solution.parent
            arr.append(solution)
        reversedArr = arr[::-1]
        return reversedArr

    @staticmethod
    def astar(initialState):
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
            selected = frontier[0]
            if DEBUG:
                print('level: ' + str(selected.level) + ',totalVisited: ' + str(totalVisited) + ',len(frontier): ' + str(len(frontier)))
                sys.stdout.flush()
                L2.append(int(selected.level))
                L3.append(int(len(frontier)))
            del frontier[0]
            if selected.isSolved(): #Make sure that you uncomment the necessary line to see the plot.
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
                    bisect.insort(frontier, b)
        print('no solution. :(')
        print('Total visited: ' + str(totalVisited))















