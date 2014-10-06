'''NAMES OF THE AUTHOR(S): ...'''

from search import *
from itertools import chain

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
        total = 0
        for row in self.array:
            total += len([tile for tile in row if tile]) 
        return total == 1

    # returns a list of non-empty neighbours of (i,j)
    def getNeighbours(self, i, j):
        neighbours = []

        if i > 0 and self.array[i-1][j]: neighbours.append(self.array[i-1][j])
        if j > 0 and self.array[i][j-1]: neighbours.append(self.array[i][j-1])
        if i < (len(self.array) - 1): neighbours.append(self.array[i+1][j])
        if j < (len(self.array[0]) - 1): neighbours.append(self.array[i][j+1])

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
        for i in range(len(state.array)):
            for j in range(len(state.array[0])):
                if state.array[i][j] == () :
                    neighbours = state.getNeighbours(i, j)
                    if len(neighbours) > 1:
                        nextState = State()
                        for row in state.array:
                            nextState.appendRow([x for x in row]);
                            
                        nextState.set(i,j, tuple(chain(*neighbours)))
                        nextState.set(i+1,j, ())
                        nextState.set(i,j+1, ())
                        nextState.set(i-1,j, ())
                        nextState.set(i,j-1, ())
                        yield ((i,j), nextState)
        #yield from state.successor()

###################### Launch the search #########################
problem=Koutack(sys.argv[1])

#example of bfs search
node=breadth_first_graph_search(problem)
#example of print
path=node.path()
path.reverse()
for n in path:
    print(n.state) #assuming that the __str__ function of states output the correct format

