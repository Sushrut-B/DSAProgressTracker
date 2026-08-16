class Solution(object):
    def eventualSafeNodes(self, graph):
        V = len(graph)

        rev = [[] for _ in range(V)]
        indegree = [0] * V

        for i in range(V):
            for nei in graph[i]:
                rev[nei].append(i)
                indegree[i] += 1

        q = deque()

        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        safe = []

        while q:
            node = q.popleft()
            safe.append(node)

            for nei in rev[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        return sorted(safe)