# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        length=1
        tail=head
        while tail.next:
            tail=tail.next
            length+=1
        k=k%length
        if k==0:
            return head
        tail.next=head
        steps=length-k
        newtail=head
        for _ in range(steps-1):
            newtail=newtail.next
        newhead=newtail.next
        newtail.next=None
        return newhead