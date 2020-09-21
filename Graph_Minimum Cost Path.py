#code
'''
Given a square grid of size N, each cell of which contains integer cost which represents a cost to traverse through that cell, we need to find a path from top left cell to bottom right cell by which total cost incurred is minimum. You can move in 4 directions : up, down, left an right.

Note : It is assumed that negative cost cycles do not exist in input matrix.

Input:
The first line of input will contain number of testcases T. Then T test cases follow. Each test case contains 2 lines. The first line of each test case contains an integer N denoting the size of the grid. Next line of each test contains a single line containing N*N space separated integers depicting the cost of respective cell from (0,0) to (N,N).

Output:
For each test case output a single integer depecting the minimum cost to reach the destination.
'''

import sys 
  
# Returns cost of minimum cost path from (0,0) to (m, n) in mat[R][C] 
def minCost(cost, m, n): 
    if (n < 0 or m < 0): 
        return sys.maxsize 
    elif (m == 0 and n == 0): 
        return cost[m][n] 
    else: 
        return cost[m][n] + min(minCost(cost, m-1, n), 
                                minCost(cost, m, n-1) ) 
  
#A utility function that returns minimum of 3 integers */ 

        
n = int(input())
for i in range(n):
    m = int(input())
    arr = list(map(int, input().split()))
    ma = [[0 for j in range(m)] for i in range(m)]
    for i in range(len(arr)):
        j = i%m
        k = i//m
        ma[k][j] = arr[i]
    print(minCost(ma, m-1, m-1))
