class Solution(object):
    def solve(self, board):
        n=len(board)
        m=len(board[0])
        def dfs(r,c):
            if r < 0 or r >= n or c < 0 or c >= m:
                return 
            if board[r][c] != "O":
                return 
            board[r][c] = "#"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for i in range(n):
            if board[i][0]=="O":
                dfs(i,0)
            if board[i][m-1]=="O":
                dfs(i,m-1)
        for j in range(m):
            if board[0][j] == "O":
                dfs(0,j)
            if board[n-1][j]=="O":
                dfs(n-1,j)
        for i in range(n):
            for j in range(m):
                if board[i][j]=="O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
        return board

        