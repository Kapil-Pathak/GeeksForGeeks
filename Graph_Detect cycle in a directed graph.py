# Your task is to complete this function
# Function should return True/False or 1/0
# Graph(graph) is a defaultict of type List
# n is no of Vertices
'''
Given a Directed Graph. Check whether it contains any cycle or not.

Input: The first line of the input contains an integer 'T' denoting the number of test cases. Then 'T' test cases follow. Each test case consists of two lines. Description of testcases is as follows: The First line of each test case contains two integers 'N' and 'M'  which denotes the no of vertices and no of edges respectively. The Second line of each test case contains 'M'  space separated pairs u and v denoting that there is an uni-directed  edge from u to v .

Output:
The method should return 1 if there is a cycle else it should return 0

'''
def util(g, s, visited, rek):
    visited[s] = 1
    rek[s] = 1
    for i in g[s]:
        if visited[i] == 0:
            if util(g, i, visited, rek):
                return 1
        elif rek[i] == 1:
            return 1
    rek[s] = 0
    return 0
    
def isCyclic(n, g):
    '''
    :param g: given adjacency list representation of graph
    :param n: no of nodes in graph
    :return:  boolean (whether a cycle exits or not)
    '''
    visited = [0]*n
    rek = [0]*n
    for i in range(n):
        if visited[i] == 0:
            if util(g, i, visited, rek):
                return 1
    return 0
    # Code here



#{ 
#  Driver Code Starts

from collections import defaultdict

def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        # graph[arr[i + 1]].append(arr[i])
        i += 2

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n,e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        if isCyclic(n, graph):
            print(1)
        else:
            print(0)
# } Driver Code Ends
