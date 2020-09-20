'''
Given an integer. Find how many structurally unique binary search trees are there that stores the values from 1 to that integer (inclusive).
'''

def numTrees(N):
    d = [0]*(N+1)
    d[0] = 1
    d[1] = 1
    for i in range(2, N+1):
        for j in range(1, i+1):
            d[i] = d[i] + (d[j-1]*d[i-j])
    return (d[N]%1000000007)
