#code
"""
You are given an array A of size N. The array contains integers and is of even length. The elements of the array represent N coin of values V1, V2, ....Vn. You play against an opponent in an alternating way.

In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and receives the value of the coin.

You need to determine the maximum possible amouint of money you can win if you go first.

Input:
The first line of input contains T denoting the number of testcases. T testcases follow. Each testcase contains two lines of input. The first line contains N denoting the size of the array. The second line contains N elements of the array.

Output:
For each testcase, in a new line, print the maximum amout.

Constraints:
1 <= T <= 100
2 <= N <= 100
1 <= Ai <= 106

Examples:
Input:
2
4
5 3 7 10
4
8 15 3 7
Output:
15
22

Explanation:
Testcase1: The user collects maximum value as 15(10 + 5)
Testcase2: The user collects maximum value as 22(7 + 15)

"""


def optimalStrategyOfGame(arr, n):
    b = [[0 for j in range(n)] for i in range(n)]
    for gap in range(n):
        for j in range(gap, n):
            i = j - gap
            x = 0
            y = 0
            z = 0
            if (i<=(j-2)):
                x = b[i][j-2]
            if (i+1<= (j-1)):
                y = b[i+1][j-1]
            if ((i+2)<= j):
                z = b[i+2][j]
            b[i][j] = max(arr[i]+min(z,y), arr[j]+min(x,y))
    return b[0][n-1]
N = int(input())
for i in range(N):
    n = int(input())
    a = list(map(int, input().split()))
    print(optimalStrategyOfGame(a, n))
    
