class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        rows=len(image)
        cols=len(image[0])
        
        oldColour=image[sr][sc]

        if oldColour == newColor:
            return image

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            if image[r][c] != oldColour:
                return

            if image[r][c] == oldColour:
                image[r][c] = newColor

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        dfs(sr,sc)
        return image

