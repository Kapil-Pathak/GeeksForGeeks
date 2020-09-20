#code
"""
Given a string str, find length of the longest repeating subseequence such that the two subsequence don’t have same string character at same position, i.e., any i’th character in the two subsequences shouldn’t have the same index in the original string.

Input:

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The first line of each test case contains an integer N denoting the length of string str.

The second line of each test case contains the string str consisting only of lower case english alphabets.

Output:

Print the length of the longest repeating subsequence for each test case in a new line.
"""
def fun(s, m, n):
    if m == 0 or n == 0:
        return 0
    if s[m-1] == s[n-1] and m!=n:
        return fun(s, m-1, n-1)+1

    return max(fun(s, m-1, n), fun(s, m, n-1))
        
n = int(input())
for i in range(n):
    n1 = int(input())
    s = input()
    print(fun(s, n1, n1))
