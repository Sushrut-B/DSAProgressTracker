from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):

        n = len(grid)

        # Start or destination blocked
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        # Single-cell matrix
        if n == 1:
            return 1

        q = deque()
        q.append((0, 0, 1))

        grid[0][0] = 1  # mark visited

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        while q:

            r, c, dist = q.popleft()

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < n:

                    if grid[nr][nc] == 0:

                        if nr == n-1 and nc == n-1:
                            return dist + 1

                        grid[nr][nc] = 1
                        q.append((nr, nc, dist + 1))

        return -1