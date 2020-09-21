# Your task is to complete this function
'''
Given an array of integers. Find the minimum number of swaps required to sort the array in non-decreasing order.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains an integer N denoting the no of element of the array A[ ]. In the next line are N space separated values of the array A[ ] .

Output:
For each test case in a new line output will be an integer denoting  minimum umber of swaps that are  required to sort the array.
'''


# return the minimum number of swaps required to sort the arra
def minSwaps(arr, N):
    vis = [False]*N
    arrpos = [*enumerate(arr)]
    res = 0
    arrpos.sort(key =lambda it:it[1])
    for i in range(N):
        if vis[i] or arrpos[i][0] == i:
            continue
        cycle = 0
        j = i
        while(vis[j] == False):
            vis[j] = True
            j = arrpos[j][0]
            cycle+=1
        if cycle>0:
            res += (cycle-1)
    return res
    # Code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(minSwaps(arr, n))

# } Driver Code Ends
