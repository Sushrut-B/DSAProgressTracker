from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        n = len(mat)
        m = len(mat[0])

        q = deque()
        dist = [[-1] * m for _ in range(n)]

        # Put all 0s into queue
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i, j))
                    dist[i][j] = 0

        # Multi-source BFS
        while q:
            r, c = q.popleft()

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < m:
                    if dist[nr][nc] == -1:
                        dist[nr][nc] = dist[r][c] + 1
                        q.append((nr, nc))

        return dist