#code
"""
Given a 2D screen, location of a pixel in the screen ie(x,y) and a color(K), your task is to replace color of the given pixel and all adjacent(excluding diagonally adjacent) same colored pixels with the given color K.

Example:

{{1, 1, 1, 1, 1, 1, 1, 1},
{1, 1, 1, 1, 1, 1, 0, 0},
{1, 0, 0, 1, 1, 0, 1, 1},
{1, 2, 2, 2, 2, 0, 1, 0},
{1, 1, 1, 2, 2, 0, 1, 0},
{1, 1, 1, 2, 2, 2, 2, 0},
{1, 1, 1, 1, 1, 2, 1, 1},
{1, 1, 1, 1, 1, 2, 2, 1},
 };

 x=4, y=4, color=3 

{{1, 1, 1, 1, 1, 1, 1, 1},
{1, 1, 1, 1, 1, 1, 0, 0},
{1, 0, 0, 1, 1, 0, 1, 1}, 
{1, 3, 3, 3, 3, 0, 1, 0},
{1, 1, 1, 3, 3, 0, 1, 0},
{1, 1, 1, 3, 3, 3, 3, 0},
{1, 1, 1, 1, 1, 3, 1, 1},
{1, 1, 1, 1, 1, 3, 3, 1}, };

Note: Use zero based indexing.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. The first line of each test case contains Two integers N and M denoting the size of the matrix. Then in the next line are N*M space separated values of the matrix. Then in the next line are three values x, y and K.
"""


def util(M, x, y, prev, k):
    if x<0 or x>(len(M)-1) or y<0 or y>(len(M[0])-1) or (M[x][y]!= prev) or (M[x][y]== k):
        return M
    M[x][y] = k
    M = util(M, x+1, y, prev, k)
    M = util(M, x-1, y, prev, k)
    M = util(M, x, y+1, prev, k)
    M = util(M, x, y-1, prev, k)
    return M
     
def flood(M, x, y, k):
    prev = M[x][y]
    M = util(M, x, y, prev, k)
    for i in range(len(M)):
        for j in range(len(M[0])):
            if i == len(M)-1 and j == len(M[0])-1:
                print(M[i][j], end = "\n")
            else:
                print(M[i][j], end = " ")
n = int(input())
for i in range(n):
    n1, m1 = map(int, input().split())
    arr = list(map(int, input().split()))
    x, y, K = map(int, input().split())
    M = []
    a = []
    for i in range(len(arr)):
        if (i+1)%m1 == 0:
            a.append(arr[i])
            M.append(a)
            a = []
            
        else:
            a.append(arr[i])
    flood(M, x, y, K)
