#User function Template for python3
class Solution:
    def print2largest(self, arr):
        # Code Here
        if len(arr) < 2:
            return -1
        
        maxi1 = float('-inf')
        maxi2 = float('-inf')
        
        for i in arr:
            if i > maxi1:
                maxi2 = maxi1
                maxi1 = i
            elif i > maxi2 and i != maxi1:
                maxi2 = i
        
        return maxi2


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends
