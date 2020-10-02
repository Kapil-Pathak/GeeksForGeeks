"""
Consider a game where a player can score 3 or 5 or 10 points in a move. Given a total score n, find the number of distinct combinations to reach the given score.

Input:
The first line of input contains an integer T denoting the number of test cases. T test cases follow. The first line of each test case is n.

Output:
For each testcase, in a new line, print the number of ways/combinations to reach the given score.
"""
#code
def count(n):
    val = [0]*(n+1)
    val[0] =1
    for i in range(3,n+1):
        val[i] += val[i-3]
    for i in range(5,n+1):
        val[i] += val[i-5]
    for i in range(10,n+1):
        val[i] += val[i-10]
    return val[n]
n = int(input())
for i in range(n):
    n1 = int(input())
    print(count(n1))
