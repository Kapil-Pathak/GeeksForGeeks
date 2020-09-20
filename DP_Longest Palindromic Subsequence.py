#code
"""
Given a String, find the longest palindromic subsequence

Input:
The first line of input contains an integer T, denoting no of test cases. The only line of each test case consists of a string S(only lowercase)

Output:
Print the Maximum length possible for palindromic subsequence.
"""
def fun(s):
    n = len(s)
    A = [[ 0 for i in range(n)] for j in range(n)]
    for i in range(n):
        A[i][i] = 1
    for cl in range(2, n+1):
        for i in range(n-cl+1):
            j = i+cl-1
            if s[i] == s[j] and cl==2:
                A[i][j] = 2
            elif s[i] == s[j]:
                A[i][j] = A[i+1][j-1]+1
            else:
                A[i][j] = max(A[i][j-1], A[i+1][j])
                
    return A[0][n-1]
n = int(input())
for i in range(n):
    s = input()
    print(fun(s))
