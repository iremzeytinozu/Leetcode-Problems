class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        dp = [0] * COLS
        dp[COLS - 1] = 1

        for row in reversed(range(ROWS)):
            for col in reversed(range(COLS)):
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0
                elif col + 1 < COLS:
                    dp[col] = dp[col] + dp[col + 1]
        
        return dp[0]
        