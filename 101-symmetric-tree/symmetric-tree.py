# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.check(left.left,right.right) and self.check(left.right,right.left)
        
    def isSymmetric(self, root):
        if not root:
            return True
        return self.check(root.left,root.right)