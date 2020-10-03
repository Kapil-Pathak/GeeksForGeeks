"""
Given a set of N items, each with a weight and a value, and a weight limit W. Find the maximum value of a collection containing any of the N items any number of times so that the total weight is less than or equal to W.
"""

def knapSack(self, N, W, val, wt):
        dp = [0]*(W+1)
        for i in range(W+1):
            for j in range(N):
                if wt[j]<=i:
                    dp[i] = max(dp[i], val[j]+dp[i-wt[j]])
        return dp[W]
