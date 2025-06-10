from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque()
        time = 0
        fresh = 0

        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for row in range(ROWS):
            for col in range(COLS):
                if grid [row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    queue.append([row, col])        
        
        while queue and fresh > 0:
            for i in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in neighbors:
                    r, c = dr + row, dc + col

                    if (r < 0 or r == len(grid) or
                        c < 0 or c == len(grid[0]) or
                        grid[r][c] != 1):
                        continue

                    grid[r][c] = 2
                    queue.append([r, c])
                    fresh -= 1

            time += 1
        return time if fresh == 0 else -1
                