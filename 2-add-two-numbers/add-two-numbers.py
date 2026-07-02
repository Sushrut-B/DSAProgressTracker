# Definition of singly linked list:
# class ListNode:
#     def __init__(self, x=0, next=None):
#         self.data = x
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(-1)
        temp = dummy
        carry = 0

        while l1 or l2 or carry:
            total = 0

            if l1:
                total += l1.val
                l1 = l1.next

            if l2:
                total += l2.val
                l2 = l2.next

            total += carry
            carry = total // 10

            node = ListNode(total % 10)
            temp.next = node
            temp = temp.next

        return dummy.next