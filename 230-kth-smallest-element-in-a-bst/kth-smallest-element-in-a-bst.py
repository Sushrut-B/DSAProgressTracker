# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        def inorder(node,values):
            if node:
                inorder(node.left,values)
                values.append(node.val)
                inorder(node.right,values)
        values=[]
        inorder(root,values)
        kthsmallest=values[k-1]
        kthlargest=values[-k]
        return kthsmallest
