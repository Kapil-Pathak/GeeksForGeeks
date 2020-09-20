"""
Given a number N. The task is to find the nth Catalan number.
The first few Catalan numbers for n = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …

Input:
The first line of input contains a single integer T which denotes the number of test cases. The first line of each test case contains a single integer N.

Output:
For each test case, in a new line print the Catalan number at position N.
"""

def cat(n):
    if n<=1:
        return 1
    res = [0]*(n+1)
    res[1] = 1
    res[0] = 1
    for i in range(2, n+1):
        res[i] = 0
        for j in range(i):
            res[i] = res[i] + res[j]*res[i-j-1]
    return res[n]
    
n = int(input())
for i in range(n):
    m = int(input())
    print(cat(m))
