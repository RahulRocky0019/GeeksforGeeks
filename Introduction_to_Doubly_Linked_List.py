#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

'''
# Node Class
	class Node:
	    def __init__(self, data):   # data -> value stored in node
	        self.data = data
	        self.next = None
	        self.prev = None
'''
class Solution:
    def constructDLL(self, arr):
        # Code here
        if len(arr) == 1:
            head = Node(arr[0])
            return head
        
        n = len(arr)
        i = 1
        head = Node(arr[0])
        temp = head
        while i < n:
            new_node = Node(arr[i])
            temp.next = new_node
            new_node.prev = temp
            
            temp = temp.next
            i += 1
        
        return head


#{ 
 # Driver Code Starts.
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.prev = None
    
def printList(node):
    tmp = node
    if tmp:
        c1, c2 = 0, 0
        while tmp.next:
            c1 += 1
            tmp = tmp.next
        while tmp.prev:
            c2 += 1
            tmp = tmp.prev
        if c1 != c2:
            print("-1")
            return
    while tmp:
        print(tmp.data, end = " ")
        tmp = tmp.next
    print()

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.constructDLL(arr)
        printList(res)
# } Driver Code Ends
