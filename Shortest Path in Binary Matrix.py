from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        N = len(grid)

        queue = deque([(0, 0, 1)])  # row, col, length
        visit = set((0, 0))

        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0], 
                             [1, 1], [-1, -1], [1, -1], [-1, 1]] 

        while queue:
            row, col, length = queue.popleft()

            if(min(row, col) < 0 or
                max(row, col) >= N or
                grid[row][col]):
                continue

            if row == N - 1 and col == N - 1:
                return length

            for dr, dc in neighbors:
                if (row + dr, col + dc) not in visit:
                    queue.append((row + dr, col + dc, length + 1))
                    visit.add((row + dr, col + dc))

        return -1