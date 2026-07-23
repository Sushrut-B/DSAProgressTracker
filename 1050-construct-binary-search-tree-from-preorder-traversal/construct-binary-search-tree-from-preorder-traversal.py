# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        index = [0]
        def build(low, high):
            if index[0] == len(preorder):
                return None
            val = preorder[index[0]]
            if val < low or val > high:
                return None
            root = TreeNode(val)
            index[0] += 1
            root.left = build(low, val)
            root.right = build(val, high)
            return root
        return build(float('-inf'), float('inf'))