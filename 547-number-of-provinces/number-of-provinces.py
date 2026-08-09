class Solution(object):
    def findCircleNum(self, isConnected):
        v = len(isConnected)
        vis = [0] * v
        cnt = 0

        def dfs(node):
            vis[node] = 1

            for nei in range(v):
                if isConnected[node][nei] == 1 and not vis[nei]:
                    dfs(nei)

        for i in range(v):
            if not vis[i]:
                cnt += 1
                dfs(i)

        return cnt