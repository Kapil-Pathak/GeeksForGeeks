#code
"""
Given a chess board of order N x M and source points (s1, s2) and destination points (d1, d2). The task to find minimum number of moves required by the Knight to go to the destination cell.
Note: The chess board consists of rows numbered (1 to N) and columns (1 to M).

Input:
The first line of input contains an integer T denoting the number of testcases. Then T test cases follow. Each test case contains two lines. The first line of each testcase contains two space separated integers N and M. Then in the next line are four space separated values s1, s2 and d1, d2.

Output:
For each testcase in a new line print the minimum number of moves required by the knight to go to the destination from the source. If no such move is possible print -1.
"""


class cell:
    def __init__(self, x, y, dist=0):
        self.x = x
        self.y = y
        self.dist = dist
        
def isInside(x, y, N, M):
    if x<=N and x>=1 and y<=M and y>=1:
        return True
    else:
        return False

def fun(N, M, s1, s2, d1, d2):
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
    queue = []
    visited = [[False for j in range(M+1)] for i in range(N+1)]
    visited[s1][s2] = True
    queue.append(cell(s1,s2))
    while(len(queue)>0):
        t = queue[0]
        queue.pop(0)
        if t.x == d1 and t.y == d2:
            return t.dist
        for i in range(8):
            x = t.x+dx[i]
            y = t.y+dy[i]
            if(isInside(x, y, N, M) and not visited[x][y]): 
                visited[x][y] = True
                queue.append(cell(x, y, t.dist + 1)) 
    return -1    
T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    s1, s2, d1, d2 = map(int, input().split())
    print(fun(N, M, s1, s2, d1, d2))
