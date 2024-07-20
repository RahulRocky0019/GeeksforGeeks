#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        pre_sum = {}
        sum = 0
        max_length = 0
        
        for i in range(n):
            sum += arr[i]
            
            if sum == k:
                max_length = max(max_length, i + 1)
            
            rem = sum - k
            if rem in pre_sum:
                length = i - pre_sum[rem]
                max_length = max(max_length, length)
                
            if sum not in pre_sum:
                pre_sum[sum] = i
        
        return max_length



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends
