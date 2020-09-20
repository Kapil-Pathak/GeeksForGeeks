'''
g : adjacency list of graph
N : number of vertices

return a list containing the DFS traversal of the given graph

Given a connected undirected graph. Perform a Depth First Traversal of the graph.
Note: Use recursive approach.

Input:
The first line of the input contains an integer 'T' denoting the number of test cases. Then 'T' test cases follow. Each test case consists of two lines. Description of testcases is as follows: The First line of each test case contains two integers 'N' and 'E'  which denotes the no of vertices and no of edges respectively. The Second line of each test case contains 'E'  space separated pairs u and v denoting that there is a edge from u to v .

Output:
For each testcase, print the nodes while doing DFS starting from node 0.
'''
def df(s, visited, a, g):
    visited[s] = True
    for i in g[s]:
        if visited[i]==False:
            a.append(i)
            visited[i] = True
            df(i, visited, a, g)
def dfs(g,N):
    visited = [False]*N
    a = []
    a.append(0)
    df(0, visited, a, g)
    return a
