# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLL(self,head):
        if not head:
            return None
        prev=None
        curr=head
        while curr:
            front=curr.next
            curr.next=prev
            prev=curr
            curr=front
        return prev

    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        newHead=self.reverseLL(slow.next)
        first=head
        second=newHead
        while second:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        return True