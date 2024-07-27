#User function Template for python3
from collections import defaultdict

class Solution:
    def substrCount (self,s, k):
        # your code here
        def atmost_k_distnct(s, k):
            if k == 0:
                return 0
            
            freq = defaultdict(int)
            l, r = 0, 0
            distinct = 0
            result = 0
            
            for r in range(len(s)):
                if freq[s[r]] == 0:
                    distinct += 1
                freq[s[r]] += 1
                
                while distinct > k:
                    freq[s[l]] -= 1
                    if freq[s[l]] <= 0:
                        distinct -= 1
                    l += 1
                
                result += r - l + 1
            
            return result
        
        result = atmost_k_distnct(s, k) - atmost_k_distnct(s, k - 1)
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
# } Driver Code Ends
