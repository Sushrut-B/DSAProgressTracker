# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseLinkedList(self, head):
        # Initialize previous pointer as None
        prev = None
        
        # Initialize current pointer as head
        curr = head
        
        # Traverse the list until all nodes are processed
        while curr is not None:
            # Temporarily store the next node
            next_node = curr.next
            
            # Reverse the link direction
            curr.next = prev
            
            # Move 'prev' one step forward
            prev = curr
            
            # Move 'curr' one step forward
            curr = next_node
        
        # 'prev' now points to the new head after reversal
        return prev

    def isPalindrome(self, head):
        stack=[]
        temp=head
        while temp:
            stack.append(temp.val)
            temp=temp.next
        temp=head
        while temp:
            if temp.val != stack.pop():
                return False
            temp=temp.next
        return True

        