class Solution(object):
    def numEnclaves(self, mat):
        n=len(mat)
        m=len(mat[0])
        def dfs(r,c):
            if r < 0 or r >= n or c < 0 or c >= m:
                return 
            if mat[r][c] == 0:
                return 
            mat[r][c] = 0
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for i in range(n):
            if mat[i][0] == 1 : 
                dfs(i, 0)

            if mat[i][m-1] == 1 : 
                dfs(i, m - 1)

            
        for j in range(m):
            if mat[0][j] == 1 : 
                dfs(0, j)

            if mat[n-1][j] == 1 : 
                dfs(n - 1, j)
        cnt=0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    cnt+=1
        return cnt

     
   