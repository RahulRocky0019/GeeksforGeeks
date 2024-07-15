#User function Template for python3

class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        
        # Approach 1
        # GCD = 1
        # min_val = min(A, B)
        # for i in range(2, min_val + 1):
        #     if A % i == 0 and B % i == 0:
        #         GCD = i
        
        # Approach 2
        a = max(A, B)
        b = min(A, B)
        while a > 0 and b > 0:
            a, b = b, a % b
        GCD = a
        
        LCM = (A * B) // GCD
        
        return [LCM, GCD]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends
