class Solution:
    def buildTree(self, preorder, inorder):

        mp = {x: i for i, x in enumerate(inorder)}
        preIndex = [0]

        def build(left, right):

            if left > right:
                return None

            root = TreeNode(preorder[preIndex[0]])
            preIndex[0] += 1

            mid = mp[root.val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)