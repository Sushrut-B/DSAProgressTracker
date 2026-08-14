class Solution(object):
    def isBipartite(self, graph):
        V = len(graph)
        colour = [-1] * V

        def dfs(node):
            for nei in graph[node]:

                if colour[nei] == -1:
                    colour[nei] = 1 - colour[node]

                    if not dfs(nei):
                        return False

                elif colour[nei] == colour[node]:
                    return False

            return True

        for i in range(V):
            if colour[i] == -1:
                colour[i] = 0

                if not dfs(i):
                    return False

        return True