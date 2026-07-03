# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        if not head:
            return None
        temp=head
        prev=None
        while temp:
            kthNode=self.getkthNode(temp,k)
            if kthNode is None:
                if prev:
                    prev.next=temp
                break
            nextNode=kthNode.next
            kthNode.next=None
            newHead=self.reverseLL(temp)
            if temp == head:
                head=newHead
            else:
                prev.next=newHead
            prev=temp
            temp.next=nextNode
            temp=nextNode
        return head
    def getkthNode(self,temp,k):
        if temp is None:
            return None
        k-=1
        while temp and k>0:
            temp=temp.next
            k-=1
        return temp
    def reverseLL(self,head):
        if head is None:
            return None
        prev=None
        curr=head
        while curr:
            front=curr.next
            curr.next=prev
            prev=curr
            curr=front
        return prev

