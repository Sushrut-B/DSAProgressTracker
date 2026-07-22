class Solution:
    def buildTree(self, inorder, postorder):

        mp = {x: i for i, x in enumerate(inorder)}
        postIndex = [len(postorder) - 1]

        def build(left, right):

            if left > right:
                return None

            root = TreeNode(postorder[postIndex[0]])
            postIndex[0] -= 1

            mid = mp[root.val]

            # IMPORTANT: Build right first
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)