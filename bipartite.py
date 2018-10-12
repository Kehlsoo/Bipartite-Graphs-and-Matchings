'''
Bipartite Graphs and Matchings

This tests whether or not a given bipartite graph has
a perfect matching and it determines whether or not a graph is bipartite.

@author: Kehlsey Lewis
'''


'''
Helper method that will take a list and turn into a set without duplicates
'''


def make_set(lists):
    
    # creating an empty set to add the new elements to
    set = []
    
    # goes through the given list and removes duplicates and adds them to the new set
    for x in lists:
        if x not in set:
            set.append(x)
    return set


'''
Takes in a list as its input, and then returns the power set of
that list.
'''


def power(list):
    # creates a set containing the empty set
    answer = [[]]
    
    # going through the set and creating mixes of the elements
    for y in list:
        for z in list:
            # adding the mix into list, and adding it to the answer list
            tempa = []
            tempa.append(y)
            tempa.append(z)
            answer.append(tempa)
       
    # removing duplicate sets from the answer list and putting them into a new list
    temp = []
    for item in answer:
        if sorted(item) not in temp:
            temp.append(sorted(item))
    
    # making the lists inside the temp list into sets    
    temp2 = []    
    for a in temp:
        if make_set(a) not in temp2:
            temp2.append(make_set(a))
    
    # returning temp2 because it contains the full list of powersets without duplicates
    return temp2


'''
Takes in a bipartite graph as its input, and
then returns the partite sets of the graph
'''


def partite_sets(graph):
    x = []
    y = []
    answer = []
     
    # first checks the key
    for node in graph.keys():
         
        #adds key to x if not found
        if ((node not in x) and (node not in y)):
            x.append(node)
             
            #adds the connecting vertex to y
            for edge in graph[node]:
                if ((edge not in x) and (edge not in y)):
                    y.append(edge)
         
        #key found in x
        elif node in x:
            for edge in graph[node]:
                if ((edge not in x) and (edge not in y)):
                    y.append(edge)
             
        #key found in y    
        else:
            for edge in graph[node]:
                if edge not in x:
                    x.append(edge)
        
    answer.append(x)
    answer.append(y)           
    return answer


'''
Takes in a graph as its input, and then determines
whether or not the graph is bipartite.
'''

def is_bipartite(graph):
    
    x = []
    y = []
    answer = True
    
    #not bipartite if empty
    if graph == {}:
        answer = False
        
    # first checks the key
    for node in graph.keys():
         
        #adds key to x if not found
        if ((node not in x) and (node not in y)):
            x.append(node)
              
            #adds the connecting vertex to y
            for edge in graph[node]:
                if edge not in y:
                    y.append(edge)
         
        #key found in x
        elif node in x:
            for edge in graph[node]:
                if edge in x: # false if connecting vertex also in x
                    answer = False
                    
                elif edge not in y:
                    y.append(edge)
             
        #key found in y    
        else:
            for edge in graph[node]:
                if edge in y:
                    answer = False #false if connecting vertex also in y
                elif edge not in x:
                    x.append(edge)
    
    return answer


'''
Takes in a bipartite graph as its input, and then
determines whether or not the graph has a perfect matching.
'''


def is_perfect(graph):
    
    answer = True
    temp = partite_sets(graph) #turning the given graph into partite sets
    x = temp[0]
    y = temp[1]
    
    if len(x) != len(y):
        answer = False #not perfect if lengths are different

    return answer
