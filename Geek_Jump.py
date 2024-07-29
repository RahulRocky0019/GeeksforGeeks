#User function Template for python3

class Solution:
    def minimumEnergy(self, height, n):
        # Code here
        dp = [0] * n
        
        for i in range(1, n):
            step_1 = dp[i - 1] + abs(height[i] - height[i - 1])
            if i == 1:
                step_2 = float('inf')
            else:
                step_2 = dp[i - 2] + abs(height[i] - height[i - 2])
            dp[i] = min(step_1, step_2)
        
        return dp[n - 1]
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        height = list(map(int, input().split()))
        ob = Solution()
        print(ob.minimumEnergy(height, n))
# } Driver Code Ends
