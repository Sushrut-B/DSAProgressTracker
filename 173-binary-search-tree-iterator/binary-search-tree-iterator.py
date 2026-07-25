# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        self.values = []
        self.index = -1

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.values.append(node.val)
            inorder(node.right)

        inorder(root)

    def hasNext(self):

        return self.index + 1 < len(self.values)

    def next(self):

        self.index += 1
        return self.values[self.index]