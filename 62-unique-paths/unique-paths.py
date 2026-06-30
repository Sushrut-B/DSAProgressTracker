class Solution:
    # Function to solve the problem using tabulation
    def func(self, m, n, dp):
        # Loop through the grid using two nested loops
        for i in range(m):
            for j in range(n):
                # Base condition
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    """Skip the rest of the loop and 
                    continue with the next iteration."""
                    continue

                """ Initialize variables to store the number
                of ways from cell above (up) and left (left)"""
                up = 0
                left = 0

                """ If we are not at first row (i > 0), update 
                'up' with the value from the cell above"""
                if i > 0:
                    up = dp[i - 1][j]

                """ If we are not at the first column (j > 0),
                update 'left' with value from the cell to left"""
                if j > 0:
                    left = dp[i][j - 1]

                """ Calculate the number of ways to reach the
                current cell by adding 'up' and 'left'"""
                dp[i][j] = up + left

        # The result is stored in bottom-right cell (m-1, n-1)
        return dp[m - 1][n - 1]

    """ Function to count the total ways
    to reach (0,0) from (m-1,n-1)"""
    def uniquePaths(self, m, n):
        """ Initialize a memoization table (dp)
        to store the results of subproblems"""
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # Return the total count (0-based indexing)
        return self.func(m, n, dp)

if __name__ == "__main__":
    m = 3
    n = 2

    # Create an instance of Solution class
    sol = Solution()

    # Call the uniquePaths function and print the result
    print("Number of ways:", sol.uniquePaths(m, n))
