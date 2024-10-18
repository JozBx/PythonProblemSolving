'''
https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/

 Dijkstra’s Algorithm using Adjacency Matrix :

     The idea is to generate a  SPT (shortest path tree)  with a given source as a root. Maintain an Adjacency Matrix with two sets, 

         one set contains vertices included in the shortest-path tree, 
         other set includes vertices not yet included in the shortest-path tree. 

     At every step of the algorithm, find a vertex that is in the other set (set not yet included) and has a minimum distance from the source. 

Algorithm :

    Create a set sptSet (shortest path tree set) that keeps track of vertices included in the shortest path tree, i.e., 
     whose minimum distance from the source is calculated and finalized. Initially, this set is empty.
    Assign a distance value to all vertices in the input graph. Initialize all distance values as INFINITE . 
    Assign the distance value as 0 for the source vertex so that it is picked first.
    While sptSet doesn’t include all vertices
        Pick a vertex u that is not there in sptSet and has a minimum distance value.
        Include u to sptSet .
        Then update the distance value of all adjacent vertices of u .
            To update the distance values, iterate through all adjacent vertices.
            For every adjacent vertex v, if the sum of the distance value of u (from source) and weight of edge u-v , 
             is less than the distance value of v , then update the distance value of v . 

Note: We use a boolean array sptSet[] to represent the set of vertices included in SPT . If a value sptSet[v] is true, 
then vertex v is included in SPT , otherwise not. Array dist[] is used to store the shortest distance values of all vertices. 

g.graph = [
            [0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]
            ]

Vertex      Distance from Source
0                 0
1                 4
2                 12
3                 19
4                 21
5                 11
6                 9
7                 8
8                 14
'''

def find_shortest_path(d, s_path, current_key, current_sum, list_keys):              
    
    for next_key, value in d[current_key].items():
        if next_key not in list_keys:
            if next_key not in s_path.keys():
                s_path[next_key] = current_sum+value
            else:
                if s_path[next_key] > current_sum+value:
                    s_path[next_key] = current_sum+value
            if next_key in d:  # Continue to the next key in the dictionary if it exists
                new_list_keys = list_keys.copy()
                new_list_keys.append(next_key)
                find_shortest_path(d, s_path, next_key, current_sum + value, new_list_keys)


def shortest_paths(start: str, entry: list) -> list:

    length = len(entry[0])
    paths = {}
    # list_paths_temp = []
    # list_paths = []

    for i in range(length):
        for j in range(i, length):
            if entry[i][j] > 0:
                if str(i) not in paths.keys() and str(j) not in paths.keys():
                    paths[str(i)] = {str(j): entry[i][j]}
                    paths[str(j)] = {str(i): entry[i][j]}
                elif str(j) in paths.keys() and str(i) in paths.keys():
                    paths[str(j)].update({str(i): entry[i][j]})
                    paths[str(i)].update({str(j): entry[i][j]})
                elif str(j) in paths.keys():
                    paths[str(j)].update({str(i): entry[i][j]})
                    paths[str(i)] = {str(j): entry[i][j]}
                else:
                    paths[str(i)].update({str(j): entry[i][j]})
                    paths[str(j)] = {str(i): entry[i][j]}
                # list_paths_temp.append([str(i), str(j)])

    shortest_paths = {}
    find_shortest_path(paths, shortest_paths, start, 0, list_keys=[start])
        
    print(paths)
    print(shortest_paths)
    # for couple in 

    return


graph = [
    [0, 4 , 0, 00, 00, 00, 0, 8 , 0],
    [4, 00, 8, 00, 00, 00, 0, 11, 0],
    [0, 8 , 0, 7 , 00, 4 , 0, 00, 2],
    [0, 00, 7, 00, 9 , 14, 0, 00, 0],
    [0, 00, 0, 9 , 00, 10, 0, 00, 0],
    [0, 00, 4, 14, 10, 00, 2, 00, 0],
    [0, 00, 0, 00, 00, 2 , 0, 1 , 6],
    [8, 11, 0, 00, 00, 00, 1, 00, 7],
    [0, 00, 2, 00, 00, 00, 6, 7 , 0]
    ]

shortest_paths(start="0", entry=graph)