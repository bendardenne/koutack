'''NAMES OF THE AUTHOR(S): ...'''

import re
from search import *


######################  State class  ###############################

class State :

    def __init__(self):
        self.array = []
        self.rowLength = 0
    
    
    def addTile(self, tile):
        self.array.append(tile)


    def isSolution(self):
        return len([tile for tile in self.array if tile]) == 1


    def getNeighbours(self, i):
        neighbours = []
        
        if (i+1) % self.rowLength != 0:             #dont get next line
            neighbours += self.getValidTile(i+1)

        if (i) % self.rowLength != 0:
            neighbours += self.getValidTile(i-1)    #dont get previous line
        
        neighbours += self.getValidTile(i+self.rowLength)
        neighbours += self.getValidTile(i-self.rowLength)
    
        return [x for x in neighbours if x]
    
    def getValidTile(self, pos):
        if pos < len(self.array) and pos >= 0:
            return self.array[pos]
        else:
            return ()

    
    def __str__(self):
        string = ""
        i = 1
        print(self.rowLength)
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

        return string[:-1]
         
######################  Implement the search #######################

class Koutack(Problem):

    def __init__(self,init):
        self.initial = State()
        f = open(init, 'r')
        line = []
        
        for line in f:
            for tile in line.split():
                if (tile == "."):
                    self.initial.addTile(())
                else:
                    self.initial.addTile((tile[0],))
        self.initial.rowLength = len(line)/2 + 1    #no /n on EOF
    
        print(self.initial)
        self.successor(self.initial)
        
    
    def goal_test(self, state):
        return state.isSolution()


    def successor(self, state):
        for i in range(len(state.array)):
            #print(i)
            print(state.getNeighbours(i))
            if not state.array[i] :#and state.getNeighbours(i):
                
                neighbours = state.getNeighbours(i)
                if neighbours:
                    nextState = State()
                    nextState.array = state.array[:]  #copy the new state
                    #nextState.play(i)
    

        return 0
        

###################### Launch the search #########################
problem=Koutack(sys.argv[1])

"""    
#example of bfs search
node=breadth_first_graph_search(problem)
#example of print
path=node.path()
path.reverse()
for n in path:
    print(n.state) #assuming that the __str__ function of states output the correct format

   """     
