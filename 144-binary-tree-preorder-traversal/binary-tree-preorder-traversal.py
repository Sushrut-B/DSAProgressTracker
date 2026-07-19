# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

    # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data= val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root):
        res=[]
        def func(node):
            if not node:
                return 
            res.append(node.val)
            func(node.left)
            func(node.right)
            
            
        func(root)
        return res