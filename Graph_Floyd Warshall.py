#code
"""
The problem is to find shortest distances between every pair of vertices in a given edge weighted directed Graph. The Graph is represented as Adjancency Matrix, and the Matrix denotes the weight of the edegs (if it exists) else INF (1e7).

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. The first line of each test case contains an integer V denoting the size of the adjacency matrix. The next V lines contain V space separated values of the matrix (graph). All input will be integer type.

Output:
For each test case output will be V*V space separated integers where the i-jth integer denote the shortest distance of ith vertex from jth vertex. For INT_MAX integers output INF.

"""
def floydWarshall(graph): 
    V = len(graph)
    dist = graph
    for k in range(V):  
        for i in range(V):  
            for j in range(V): 
                dist[i][j] = min(dist[i][j] ,dist[i][k]+ dist[k][j])
    return dist
INF = 10000000                       
def printSolution(dist): 
    V = len(dist)
    for i in range(V): 
        for j in range(V): 
            
            if j == V-1: 
                print(dist[i][j], end="\n")  
            else:
                print(dist[i][j], end=" ") 
n = int(input())
for i in range(n):
    n1 = int(input())
    mat = []
    for j in range(n1):
        mat.append(list(map(int, input().split())))
    dist = floydWarshall(mat)
    printSolution(dist)
    
    
