"""
Given a M X N matrix with your initial position at the top-left cell, find the number of possible unique paths to reach the bottom-right cell of the matrix from the initial position.

Note: Possible moves can be either down or right at any point in time, i.e., we can move to matrix[i+1][j] or matrix[i][j+1] from matrix[i][j].

Input:
The first line contains an integer T, depicting the total number of test cases. Then following T lines contain two integers M and N depicting the size of the grid.

Output:
Print the number of unique paths to reach the bottom-right cell from the top-left cell.

"""


n = int(input())
def countMat(n1, n2):
    count = [[ 0 for x in range(n2)] for y in range(n1)]
    for i in range(n1):
        count[i][0] = 1
    for i in range(n2):
        count[0][i] = 1
    for i in range(1, n1):
        for j in range(n2):
            count[i][j] = count[i-1][j] + count[i][j-1]
    return count[n1-1][n2-1]
                
for i in range(n):
    size_array = list(map(int, input().split()))
    print(countMat(size_array[0], size_array[1]))
