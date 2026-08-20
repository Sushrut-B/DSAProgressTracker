class Solution(object):
    def minimumEffortPath(self, heights):
        n = len(heights)
        m = len(heights[0])

        dist = [[10**9] * m for _ in range(n)]
        dist[0][0] = 0

        pq = [(0, 0, 0)]   # effort, row, col

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while pq:

            effort, r, c = heapq.heappop(pq)

            if r == n - 1 and c == m - 1:
                return effort

            if effort > dist[r][c]:
                continue

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < m:

                    diff = abs(heights[r][c] - heights[nr][nc])

                    newEffort = max(effort, diff)

                    if newEffort < dist[nr][nc]:

                        dist[nr][nc] = newEffort

                        heapq.heappush(
                            pq,
                            (newEffort, nr, nc)
                        )

        return 0