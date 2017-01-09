import random
import copy
import math

class PuzzleState:
    matrix = None # this is an integer matrix
    emptyIndex = (0,0)
    originalPlaces = {}
    h = None

    def __init__(self, matrix, emptyIndex = None):
        if emptyIndex == None:
            for i,lst in enumerate(matrix):
                for j,value in enumerate(lst):
                    if value == 0:
                        self.emptyIndex = (i,j)
        else:
            self.emptyIndex = emptyIndex

        self.matrix = matrix
        self.setOriginalPlaces()

    @staticmethod
    def getRandomPuzzleState(n):
        allNumbers = range(0, n*n)
        matrix = []
        emptyIndex = (0,0)
        for i in range(n):
            line = []
            for j in range(n):
                index = random.randint(0, len(allNumbers)-1)
                element = allNumbers[index]

                if element == 0:
                    emptyIndex = (i,j)

                line.append(element)
                del allNumbers[index]
            matrix.append(line)
        return PuzzleState(matrix, emptyIndex)

    @staticmethod
    def getSolvablePuzzleState(n, hardness):
        value = 0
        matrix = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(value)
                value = value + 1
            matrix.append(temp)
        p = PuzzleState(matrix)
        arr = [p]
        for i in range(hardness):
            branches = arr[-1].getBranchPuzzleStates()
            b = random.choice(branches)
            while b in arr:
                b =  random.choice(branches)
            arr.append(b)
        return arr[-1]

    def getBranchPuzzleStates(self):
        rVal = []
        n = len(self.matrix)
        idx = self.emptyIndex

        offsets = [(-1,0),(0,-1),(0,1),(1,0)]
        for offset in offsets:
            temp =(idx[0] + offset[0], idx[1] + offset[1])
            if temp[0] >= 0 and temp[1] >= 0 and temp[0] < n and temp[1] < n:
                newEmptyIndex = copy.deepcopy(temp)
                newMatrix = copy.deepcopy(self.matrix)
                newMatrix[idx[0]][idx[1]] = newMatrix[temp[0]][temp[1]]
                newMatrix[temp[0]][temp[1]] = 0
                rVal.append(PuzzleState(newMatrix, newEmptyIndex))
        return  rVal

    def isSolved(self):
        n = len(self.matrix)
        value = 0
        for i in range(n):
            for j in range(n):
                if self.matrix[i][j] == value:
                    pass
                else:
                    return False
                value = value + 1
        return True

    def getCost_h1(self):
            misplaced = 0  # Counts the number of misplaced tiles !
            compare = -1
            m = self.matrix
            #print m
            n = len(self.matrix)
            for i in range(n):
                for j in range(n):
                    if m[i][j] != compare:
                            misplaced += 1
                    compare += 1
            #print compare
            return misplaced

    def getCost_h2(self):
            distance = -1    # Manhattan distance !
            m = self.matrix
            #print m
            n = len(self.matrix)
            for i in range(n):
                for j in range(n):
                        if m[i][j] == 0: continue
                        distance += abs(i - (m[i][j]/4)) + abs(j -  (m[i][j]%4))
            return distance

    def __lt__(self, other):
        return self.getCost_h2() <= other.getCost_h2()

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __hash__(self):
        return hash(str(self.matrix))

    def __str__(self):
        rVal = str(self.emptyIndex) + '\n'
        for line in self.matrix:
            rVal += str(line) + '\n'
        return rVal[:-1]

    def setOriginalPlaces(self):
        n = len(self.matrix)
        temp = 0
        for i in range(n):
            for j in range(n):
                self.originalPlaces[temp] = (i,j)
                temp = temp + 1


#a = PuzzleState([[1, 5, 6, 2],[9, 8, 4, 3],[12, 14, 7, 13],[15, 0, 10, 11]])
#s = a.getCost_h2()
#print s








