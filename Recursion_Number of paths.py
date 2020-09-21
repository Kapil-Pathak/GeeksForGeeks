#code
"""
MxN matrix with the constraints that from each cell you can either move to right or down.

Input:
The first line of input contains an integer T, denoting the number of test cases. The first line of each test case is M and N, M is number of rows and N is number of columns.

Output:
For each test case, print the number of paths.
"""

def cout(m, n):
    if m == 1 or n ==1:
        return 1
    return cout(m-1, n)+cout(m, n-1) 
n = int(input())
for i in range(n):
    m, n = map(int, input().split())
    print(cout(m, n))
