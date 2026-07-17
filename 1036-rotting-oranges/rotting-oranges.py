class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        queue = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        if fresh == 0:
            return 0

        minutes = 0
        pointer = 0
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        while pointer < len(queue):
            level_size = len(queue) - pointer
            for _ in range(level_size):
                r, c = queue[pointer]
                pointer += 1

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

            if pointer < len(queue):
                minutes += 1

        return minutes if fresh == 0 else -1
