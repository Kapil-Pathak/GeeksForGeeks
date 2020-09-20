#User function Template for python3
class Solution:
	def getNthUglyNo(self,n):
		# code here
		a = [0]*n
		a[0] = 1
		s2 = 2
		s3 = 3
		s5 = 5
		i2 = i3 = i5 =0
		for i in range(1, n):
		    a[i] = min(s2, s3, s5)
		    if a[i] == s2:
		        i2+=1
                s2 = a[i2]*2
            elif a[i] == s3:
		        i3+=1
                s3 = a[i3]*3
            elif a[i] == s5:
		        i5+=1
                s5 = a[i5]*5
        return a[-1]



#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.getNthUglyNo(n);
        print(ans)
        tc -= 1

# } Driver Code Ends
