'''NAMES OF THE AUTHOR(S): ...'''

from search import *


######################  State class  ###############################

class State :

    def __init__(self):
        self.array = []
    
    def appendRow(self, row):
        self.array.append(row)

    def isSolution(self):
        empty = True
        for row in self.array:
            for tile in row:
                if tile:
                    if not empty:
                        return False
                    empty = False
        return  True

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
        print(self.initial.isSolution()) 
        
    
    def goal_test(self, state):
        return state.isSolution()


    def successor(self, state):
        pass
        

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
