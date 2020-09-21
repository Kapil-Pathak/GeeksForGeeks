'''
Imagine you have a special keyboard with the following keys: 

Key 1:  Prints 'A' on screen
Key 2: (Ctrl-A): Select screen
Key 3: (Ctrl-C): Copy selection to buffer
Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Find maximum numbers of A's that can be produced by pressing keys on the special keyboard N times. 
'''
class Solution:
    def optimalKeys(self, N):
        screen = [0]*N
        # code here
        if N<= 6: 
            return N
        for i in range(1, 7):
            screen[i-1] = i
        for i in range(7, N+1):
            screen[i-1] = 0
            for b in range(N-3, 0, -1):
                curr = (i-b-1)*screen[b-1]
                if curr>screen[i-1]:
                    screen[i-1] = curr
        return screen[N-1]
