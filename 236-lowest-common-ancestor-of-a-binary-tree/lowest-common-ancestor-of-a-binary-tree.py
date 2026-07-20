# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getPath(self, root, target, path):
        if not root:
            return False

        path.append(root)

        if root == target:
            return True

        if self.getPath(root.left, target, path) or self.getPath(root.right, target, path):
            return True

        path.pop()
        return False

    def lowestCommonAncestor(self, root, p, q):
        path1 = []
        path2 = []

        self.getPath(root, p, path1)
        self.getPath(root, q, path2)

        i = 0
        while i < len(path1) and i < len(path2):
            if path1[i] != path2[i]:
                break
            i += 1

        return path1[i - 1]