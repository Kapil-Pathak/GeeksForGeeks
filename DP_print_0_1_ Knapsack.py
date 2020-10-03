"""
Printing Items in 0/1 Knapsack
Last Updated: 04-02-2019
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the items such that sum of the weights of those items of given subset is smaller than or equal to W. You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
"""

def ksnap(val, wt, n, W):
    K = [[0 for j in range(W+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                K[i][j] = 0
            else:
                if wt[j-1]>W:
                    K[i][j] = K[i-1][j]
                else:
                    K[i][j] = max(val[i-1]+K[i-1][j-wt[j-1]], K[i-1][j])
    res = K[n][W]
    w = W
    for i in range(n, 0 ,-1):
        if res<= 0:
            break
        if res == K[i-1][w]:
            continue
        else:
            print(wt[i-1])
            res = res - val[i-1]
            w = w - wt[i-1]
