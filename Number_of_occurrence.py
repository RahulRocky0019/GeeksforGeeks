#User function Template for python3
class Solution:

	def count(self,arr, n, x):
		# code here
		
        def cond_binarysearch(arr, n, x, bias):
            low, high = 0, n - 1
            result = -1
            
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == x:
                    result = mid
                    if bias:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            
            return result
		
		
		floor = cond_binarysearch(arr, n, x, True)
		if floor == -1:
		    return 0
		ceil = cond_binarysearch(arr, n, x, False)
		
		return ceil - floor + 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends
