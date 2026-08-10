class Solution(object):
    def findOrder(self, N, prerequisites):
        adj = [[] for _ in range(N)]

        # Build directed graph
        for course, pre in prerequisites:
            adj[pre].append(course)

        vis = [0] * N
        path = [0] * N
        ans = []

        def dfs(node):
            vis[node] = 1
            path[node] = 1

            for nei in adj[node]:
                if not vis[nei]:
                    if dfs(nei):
                        return True

                elif path[nei]:
                    return True

            path[node] = 0
            ans.append(node)
            return False

        for i in range(N):
            if not vis[i]:
                if dfs(i):
                    return []

        ans.reverse()
        return ans