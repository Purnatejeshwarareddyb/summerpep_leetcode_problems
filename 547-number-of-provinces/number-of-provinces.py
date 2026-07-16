class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        def dfs(city: int):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        n = len(isConnected)
        visited = set()
        provinces = 0

        for city in range(n):
            if city not in visited:
                provinces += 1
                visited.add(city)
                dfs(city)

        return provinces
