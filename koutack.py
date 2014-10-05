'''NAMES OF THE AUTHOR(S): ...'''

from search import *
from copy import deepcopy

######################  State class  ###############################

class State :

    def __init__(self):
        self.array = []
    
    def appendRow(self, row):
        self.array.append(row)

    def set(self, x, y, val):
        #out of bounds coordinates
        if(x < 0 or y < 0 or x >= len(self.array) or y >= len(self.array[0])):
            return 
        
        self.array[x][y] = val

    def isSolution(self):
        empty = True
        for row in self.array:
            for tile in row:
                if tile:
                    if not empty:
                        return False
                    empty = False
        return True

    def successor(self):
        for i in range(len(self.array)):
            for j in range(len(self.array[0])):
                if self.array[i][j] == () :
                    neighbours = self.getNeighbours(i, j)
                    if len(neighbours) > 1:
                        nextState = deepcopy(self)
                        nextState.set(i,j, tuple(neighbours))
                        nextState.set(i+1,j, ())
                        nextState.set(i,j+1, ())
                        nextState.set(i-1,j, ())
                        nextState.set(i,j-1, ())
                        yield (None, nextState)


    # returns a list of non-empty neighbours of (i,j)
    def getNeighbours(self, i, j):
        neighbours = []

        if i > 0 and self.array[i-1][j]: neighbours += self.array[i-1][j]
        if j > 0 and self.array[i][j-1]: neighbours += self.array[i][j-1]
        if i < len(self.array) - 1 and self.array[i+1][j]: neighbours += self.array[i+1][j]
        if j < len(self.array[0]) - 1 and self.array[i][j+1]: neighbours += self.array[i][j+1] 
        
        return [ x for x in neighbours if x != () ]

    def __str__(self) :
        string = ""
        for row in self.array:
            for tile in row:
                if tile == ():
                    string += '.'
                else: 
                    string += (tile[0] if len(tile) == 1 else "[" + ",".join(tile) + "]")
                string += ' '
            string = string[:-1] + '\n'
        return string        
         
######################  Implement the search #######################

class Koutack(Problem):

    def __init__(self,init):
        self.initial = State()
        f = open(init, 'r')
        line = []
        for line in f:
            row = []
            for tile in line.split():
                if (tile == "."):
                    row.append(())
                else:
                    row.append((tile[0],))
            self.initial.appendRow(row)
    
    def goal_test(self, state):
        return state.isSolution()


    def successor(self, state):
        yield from state.successor()

###################### Launch the search #########################
problem=Koutack(sys.argv[1])

#example of bfs search
node=breadth_first_graph_search(problem)
#example of print
path=node.path()
path.reverse()
for n in path:
    print(n.state) #assuming that the __str__ function of states output the correct format

