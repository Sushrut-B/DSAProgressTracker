class Solution(object):
    def searchMatrix(self, mat, target):
        if not mat or not mat[0]:
            return False
        n=len(mat)
        m=len(mat[0])
        for i in range(n):
            for j in range(m):
                if mat[i][j] == target:
                    return True
        return False
     
        