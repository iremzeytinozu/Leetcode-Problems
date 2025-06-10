class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        islands = 0

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            queue = collections.deque()
            visit.add((r, c))
            queue.append((r, c))

            while queue: 
                row, col = queue.pop()

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(ROWS) and
                        c in range(COLS) and
                        grid[r][c] == "1" and
                        (r, c) not in visit):
                        queue.append((r, c))
                        visit.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands