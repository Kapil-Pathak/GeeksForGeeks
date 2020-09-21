#User function Template for python3
"""
Given a graph with N nodes and M directed edges. Your task is to complete the function kosaraju() which returns an integer denoting the number of strongly connected components in the graph.

Input:
The first line of input contains an integer T. Then T test cases follow. Each test case contains two integers N and M. In the next line there are M space-separated values u,v denoting an edge from u to v.

Output:
For each test case in a new line output will an integer denoting the no of strongly connected components present in the graph.

"""

# Graph (adj) is a default dict of type list
# V is the number of vertices in the graph
def DFSutil(adj, visited, v):
    visited[v] = True
    for i in adj[v]:
        if visited[i] == False:
            DFSutil(adj, visited, i)

def fillOrder(adj, visited, v, stack):
    visited[v] = True
    for i in adj[v]:
        if visited[i] == False:
            fillOrder(adj, visited, i, stack)
    stack = stack.append(v)
    
def getTranspose(adj, V):
    g = defaultdict(list)
    for i in range(V):
        for j in adj[i]:
            g[j].append(i)
    return g
        
def countSCCs (adj, V):
    stack = []
    visited = [False]*V
    for i in range(V):
        if visited[i] == False:
            fillOrder(adj, visited, i, stack)
    g = getTranspose(adj, V)
    visited = [False]*V
    count = 0
    while stack:
        i = stack.pop()
        if visited[i] == False:
            count+=1
            DFSutil(g, visited, i)
    return count






#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        i += 2


from collections import defaultdict
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        print (countSCCs(graph, n))
        
# Contributed By: Pranay Bansal
# } Driver Code Ends
