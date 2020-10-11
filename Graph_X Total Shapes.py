#code
"""
Given N * M string array of O's and X's. The task is to find the number of 'X' total shapes. 'X' shape consists of one or more adjacent X's (diagonals not included).

Input: The first line of input takes the number of test cases T. Then T test cases follow. Each of the T test cases takes 2 input lines. The first line of each test case have two integers N and M.The second line of N space separated strings follow which indicate the elements in the array.

Output:
For each testcase, print number of shapes.

Expected Time Complexity: O(N*M).
Expected Auxiliary Space: O(N*M) (recursive). 

Constraints:
1 <= T <= 100
1 <= N, M <= 50

Example:
Input:
2
4 7
OOOOXXO OXOXOOX XXXXOXO OXXXOOO
10 3
XXO OOX OXO OOO XOX XOX OXO XXO XXX OOO

Output:
4
6

Explanation:
Testcase 1: Given input is like:
OOOOXXO
OXOXOOX
XXXXOXO
OXXXOOO

So, X with same colour are adjacent to each other vertically for horizontally (diagonals not included). So, there are 4 different groups in the given matrix.

Testcase 2: Given input is like:
XXO
OOX
OXO
OOO
XOX
XOX
OXO
XXO
XXX
OOO
So, this matrix has 6 groups with is having adjacent Xs. Total number of groups is 6.

 

Company Tags
Topic Tags

If you are facing any issue on this page. Please let us know.


"""
def dfs(a, visited, i, j, N, M):
    if i<0 or i>N-1:
        return
    if j<0 or j>M-1:
        return
    if a[i][j] == 'O' or visited[i][j]:
        return
    visited[i][j] = True
    dfs(a, visited, i-1, j, N, M)
    dfs(a, visited, i+1, j, N, M)
    dfs(a, visited, i, j-1, N, M)
    dfs(a, visited, i, j+1, N, M)
    
def count(a, N, M):
    visited = [[False for j in range(M)] for i in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == False and a[i][j] == 'X':
                dfs(a, visited, i, j, N, M)
                cnt+=1
    
    return cnt
    
T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    a = list(map(str, input().split()))
    
    print(count(a, N, M))
