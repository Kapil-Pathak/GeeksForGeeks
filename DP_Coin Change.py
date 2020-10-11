"""
Given a value N, find the number of ways to make change for N cents, if we have infinite supply of each of S = { S1, S2, .. , SM } valued coins.
https://practice.geeksforgeeks.org/problems/coin-change2448/1
"""

class Solution:
    def count(self, S, m, n):
        a = [[0 for j in range(m)] for i in range(n+1)]
        for i in range(m):
            a[0][i] = 1
        for i in range(1, n+1):
            for j in range(m):
                x = a[i-S[j]][j] if i-S[j]>=0 else 0
                y = a[i][j-1] if j-1>=0 else 0
                a[i][j] = x+y
        return a[n][m-1]
        # code here 
