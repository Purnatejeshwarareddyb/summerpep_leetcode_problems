class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        
        def canReach(limit: int) -> bool:
            visited = [[False] * cols for _ in range(rows)]
            stack = [(0, 0)]
            visited[0][0] = True
            
            while stack:
                r, c = stack.pop()
                if r == rows - 1 and c == cols - 1:
                    return True
                
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                        if abs(heights[nr][nc] - heights[r][c]) <= limit:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
            return False

        left, right = 0, 10**6
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            if canReach(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans
