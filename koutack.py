'''NAMES OF THE AUTHOR(S): ...'''

from itertools import chain
from math import ceil
from search import *


######################  State class  ###############################

class State :

    def __init__(self, newArray=[], length=0):
        self.array = newArray
        self.rowLength = length
    
    
    def addTile(self, tile):
        self.array.append(tile)


    def isSolution(self):
        return len([tile for tile in self.array if tile]) == 1


    def getNeighbours(self, i):
        neighbours = []
        
        if (i+1) % self.rowLength != 0:             #dont get next line
            neighbours.append( (i+1, self.getValidTile(i+1)) )

        if (i) % self.rowLength != 0:               #dont get previous line
            neighbours.append( (i-1, self.getValidTile(i-1)) )

        neighbours.append( (i+self.rowLength, self.getValidTile(i+self.rowLength)) )
        neighbours.append( (i-self.rowLength, self.getValidTile(i-self.rowLength)) )
    
        return [x for x in neighbours if x[1]]
    
    def getValidTile(self, pos):
        if pos < len(self.array) and pos >= 0:
            return self.array[pos]
        else:
            return ()

    def play(self, neighbours, pos):
        indexes,values = zip(*neighbours)
        for index in indexes:
            self.array[index] = ()
        
        self.array[pos] = tuple(sorted(chain(*values)))


    def __str__(self):
        string = ""
        i = 1
        for tile in self.array:
            if tile == ():
                string += '.'
            else:
                string += (tile[0] if len(tile) == 1 else "[" + ",".join(tile) + "]")

            if i % self.rowLength == 0:
                string += '\n'
            else:
                string += ' '
                    
            i += 1

        return string
        
    def __hash__(self):
        return tuple(self.array).__hash__()
    
    def __eq__(self, other):
        return self.array == other.array

######################  Implement the search #######################

class Koutack(Problem):

    def __init__(self,init):
        self.visited = 0
        self.initial = State()
        f = open(init, 'r')
        line = []
        
        for line in f:
            for tile in line.split():
                if (tile == "."):
                    self.initial.addTile(())
                else:
                    self.initial.addTile((tile[0],))
        self.initial.rowLength = ceil(len(line)/2)    #no /n on EOF
        

    def goal_test(self, state):
        return state.isSolution()


    def successor(self, state):
        for index in range(len(state.array)):
            if not state.array[index] :#and state.getNeighbours(i):
                
                neighbours = state.getNeighbours(index)
                if len(neighbours) > 1:
                    nextState = State(state.array[:], state.rowLength)
                    nextState.play(neighbours,index)
                    self.visited += 1
                    yield (index, nextState)

###################### Launch the search #########################
problem=Koutack(sys.argv[1])

try :
#example of bfs search
    node = depth_first_tree_search(problem)
    path = node.path()
    path.reverse()
    for n in path:
        print(n.state) #assuming that the __str__ function of states output the correct format
except MemoryError:
    pass 
finally:
    print("Visited nodes: " + str(problem.visited))
    print("Path length" + str(len(path)))

