'''NAMES OF THE AUTHOR(S): ...'''

from search import *


######################  Implement the search #######################

class Koutack(Problem):

    def __init__(self,init):

    
    def goal_test(self, state):
        pass

        
    def successor(self, state):
        pass
        




###################### Launch the search #########################
    
problem=Koutack(sys.argv[1])
#example of bfs search
node=breadth_first_graph_search(problem)
#example of print
path=node.path()
path.reverse()
for n in path:
    print(n.state) #assuming that the __str__ function of states output the correct format

        
