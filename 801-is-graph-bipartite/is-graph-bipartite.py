class Solution(object):
    def isBipartite(self, graph):
        V = len(graph)

        colour = [-1] * V

        def bfs(start):
            q = deque([start])
            colour[start] = 1

            while q:
                node = q.popleft()

                for nei in graph[node]:
                    if colour[nei] == -1:
                        colour[nei] = 1 - colour[node]
                        q.append(nei)

                    elif colour[nei] == colour[node]:
                        return False

            return True

        for i in range(V):
            if colour[i] == -1:
                if not bfs(i):
                    return False

        return True
