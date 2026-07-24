class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        
        queue = [(0, 0, 1)]
        grid[0][0] = 1  
        
        head = 0
        while head < len(queue):
            r, c, dist = queue[head]
            head += 1
            
            if r == n - 1 and c == n - 1:
                return dist
                
            for dr, dc in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr, nc, dist + 1))
                    
        return -1
