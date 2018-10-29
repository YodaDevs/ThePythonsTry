graph = { "A" : { "B" : 1, "C":2 },
          "B" : { "D":2, "E":4 },
          "C" : { "E":2 },
          "D" : { "F": 6 },
          "E" : { "F": 7 },
          "F" : { }
          }

graph2 = {  "D" : { "A": 4, "H": 1 },
            "A" : { "H": 10, "E": 1 },
            "H" : { "E": 5, "I": 9 },
            "E" : { "F" : 3 },
            "I" : { "J" : 2 },
            "F" : { "I" : 1, "G": 7, "B": 1, "C": 3 },
            "G" : { },
            "J" : { "G" : 1 },
            "B" : { "C" : 2 },
            "C" : { } }
            

    
# Returns the shortest distance from a given node to all other possible ones.
def dijkstra(graph, source): 

    control = { }
    Current_Distance = { }
    No_Current = { }
    Not_Visited = []
    Current = source
    No_Current[Current] = 0

    
    for vertice in graph.keys():
        Not_Visited.append(vertice) # Includes vertices in the unvisited    
        Current_Distance[vertice] = float('inf') # Start the vertices as infinity

    Current_Distance[Current] =0

    Not_Visited.remove(Current)

    while Not_Visited:
        for neighbor, Weight in graph[Current].items():
             Calculated_Weight = Weight + No_Current[Current]
             if Current_Distance[neighbor] == float("inf") or Current_Distance[neighbor] > Calculated_Weight:
                 Current_Distance[neighbor] = Calculated_Weight
                 control[neighbor] = Current_Distance[neighbor]

        if control == {} : break    
        minNeighbor = min(control.items(), key=lambda x: x[1]) # Select the smallest neighbor
        Current=minNeighbor[0]
        No_Current[Current] = minNeighbor[1]
        Not_Visited.remove(Current)
        del control[Current]

    print(Current_Distance)


def dijkstra_path(graph, source, end): # Returns the shortest distance from a source node to a destination node and the path to it

    control = { }
    Current_Distance = { }
    No_Current = { }
    Not_Visited = []
    Current = source
    No_Current[Current] = 0

    
    for vertice in graph.keys():
        Not_Visited.append(vertice) # Includes the vertices in the unvisited
        Current_Distance[vertice] = float('inf') # Start the vertices as infinity

    Current_Distance[Current] = [0,source] 

    Not_Visited.remove(Current)

    while Not_Visited:
        for neighbor, Weight in graph[Current].items():
             Calculated_Weight = Weight + No_Current[Current]
             if Current_Distance[neighbor] == float("inf") or Current_Distance[neighbor][0] > Calculated_Weight:
                 Current_Distance[neighbor] = [Calculated_Weight,Current]
                 control[neighbor] = Calculated_Weight
                 print(control)
                 
        if control == {} : break    
        minNeighbor = min(control.items(), key=lambda x: x[1]) # Select the smallest neighbor
        Current=minNeighbor[0]
        No_Current[Current] = minNeighbor[1]
        Not_Visited.remove(Current)
        del control[Current]

    print("The shortest distance from %s to %s is: %s" % (source, end, Current_Distance[end][0]))
    print("The smallest path is: %s" % printPath(Current_Distance,source, end))          
    

def printPath(distances,start, end):
        if  end != start:
            return "%s -- > %s" % (printPath(distances,start, distances[end][1]),end)
        else:
            return start