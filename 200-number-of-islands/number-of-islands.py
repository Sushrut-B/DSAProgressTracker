class Solution(object):
    def numIslands(self, grid):
        n=len(grid)
        m=len(grid[0])
        cnt=0
        def dfs(r,c):
            if r<0 or r>=n or c<0 or c>=m:
                return 
            if grid[r][c]=="0":
                return
            grid[r][c] = "0"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            """dfs(r+1,c+1)
            dfs(r+1,c-1)
            dfs(r-1,c+1)
            dfs(r-1,c-1)"""
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    cnt+=1
                    dfs(i,j)
        return cnt
        