# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, key):
        def inorder(node,values):
            if node:
                inorder(node.left,values)
                values.append(node.val)
                inorder(node.right,values)
        values=[]
        inorder(root,values)
        values.sort()
        low,high=0,len(values)-1
        while low < high:
            if values[low]+values[high] == key:
                return True
            elif values[low]+values[high] > key:
                high-=1
            else:
                low+=1
        return False