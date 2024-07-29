#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

import sys
sys.setrecursionlimit(100000)

class Solution:
    def topDown(self, n):
        # Code here
        mod = 10 ** 9 + 7
        dp = [-1] * (n + 1)
        
        def fib(n):
            if n <= 1:
                return n
            if dp[n] != -1:
                return dp[n] % mod
            
            dp[n] = (fib(n - 1) + fib(n - 2)) % mod
            
            return dp[n] % mod
        
        return fib(n) % mod
    
    def bottomUp(self, n):
        # Code here
        mod = 10 ** 9 + 7
        
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % mod
        
        return dp[n] % mod
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        topDownans=ob.topDown(n);
        bottomUpans=ob.bottomUp(n);
        if(topDownans!=bottomUpans):
            print(-1)
        else:
            print(bottomUpans)
# } Driver Code Ends
