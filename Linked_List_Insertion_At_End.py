'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        # code here 
        new_node = Node(x)
        if head is None:
            return new_node
        temp = head
        
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
        
        return head

