class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        # Helper DFS function to turn connected land into water
        def dfs(r, c):
            # Base case: check grid boundaries and if the cell is water
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return
            
            # Change land to water to mark it as visited/processed
            grid[r][c] = 0
            
            # Traverse 4-directionally
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) # Left

        # Step 1: Run DFS on all land cells located on the top and bottom borders
        for c in range(cols):
            if grid[0][c] == 1:
                dfs(0, c)
            if grid[rows - 1][c] == 1:
                dfs(rows - 1, c)
                
        # Step 2: Run DFS on all land cells located on the left and right borders
        for r in range(rows):
            if grid[r][0] == 1:
                dfs(r, 0)
            if grid[r][cols - 1] == 1:
                dfs(r, cols - 1)
                
        # Step 3: Count the remaining 1s that couldn't reach any border
        enclaves_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    enclaves_count += 1
                    
        return enclaves_count
