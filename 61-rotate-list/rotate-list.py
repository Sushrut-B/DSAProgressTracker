# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        temp=head
        length=1
        while temp.next:
            temp=temp.next
            length+=1
        temp.next=head
        k=k%length
        end=length-k
        while end >0:
            temp=temp.next
            end-=1
        head=temp.next
        temp.next=None
        return head