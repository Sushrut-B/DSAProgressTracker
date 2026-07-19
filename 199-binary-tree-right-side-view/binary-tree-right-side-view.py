# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        res=[]
        def func( root, level):
            
            if root is None:
                return 
            if level == len(res):
                res.append(root.val)
            func(root.right,level+1)
            func(root.left,level+1)
            
        func(root,0)
        return res
