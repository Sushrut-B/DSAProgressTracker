# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMaxPathSum(self, root, maxi):
        if not root:
            return 0
        leftMaxPath = max(0, self.findMaxPathSum(root.left, maxi))
        rightMaxPath = max(0, self.findMaxPathSum(root.right, maxi))
        maxi[0] = max(maxi[0], leftMaxPath + rightMaxPath + root.val)
        return max(leftMaxPath, rightMaxPath) + root.val

    def maxPathSum(self, root):
        maxi = [float('-inf')]
        self.findMaxPathSum(root, maxi)
        return maxi[0]

