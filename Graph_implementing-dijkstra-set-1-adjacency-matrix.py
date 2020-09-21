
#User function Template for python3

'''
*   g: vector of vectors which represents the graph
*   src: source vertex to start traversing graph with
*   V: number of vertices

Given a graph of V nodes represented in the form of the adjacency matrix. The task is to find the shortest distance of all the vertex's from the source vertex.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first line of each test case contains an integer V denoting the size of the adjacency matrix and in the next line are V*V space-separated values, which denote the weight of an edge of the matrix (gr[i][j] represents the weight of an edge from ith node to jth node). The third line of each test case contains an integer denoting the source vertex s.

Output:
For each test, case output will be V space-separated integers where the ith integer denotes the shortest distance of the ith vertex from source vertex.




'''
import sys
def minDist(dist, V, spt):
    min = sys.maxsize
    for i in range(V):
        if min>dist[i] and spt[i] ==False:
            min = dist[i]
            min_index = i
    return min_index
    
def dijkstra(src, V, g):
    spt = [False]*V
    dist = [sys.maxsize]*V
    dist[src] = 0
    for i in range(V):
        u = minDist(dist, V, spt)
        spt[u] = True
        for v in range(V):
            if g[u][v]>0 and spt[v] == False and dist[v]>dist[u]+g[u][v]:
                dist[v]=dist[u]+g[u][v]
    return dist
    #code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

def printSolution(dist, V):
    for node in range(V):
        print(dist[node] , end=" ")
    print()


if __name__ == '__main__':
    t = int(input())
    for tst in range(t):
        v = int(input())
        graph = [[0 for column in range(v)]
                    for row in range(v)]

        lst = [int(x) for x in input().strip().split()]
        k=0
        for i in range(v):
            for j in range(v):
                graph[i][j] = lst[k]
                k+=1
        s = int(input())
        res = dijkstra(s, v, graph)
        
        printSolution (res, v)

# } Driver Code Ends
