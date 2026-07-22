class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)
            
        # 0 = unvisited, 1 = visiting (in current path), 2 = visited
        visited = [0] * numCourses
        
        def dfs(node):
            if visited[node] == 1:
                return False  # Cycle detected
            if visited[node] == 2:
                return True
                
            visited[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited[node] = 2
            return True

        for i in range(numCourses):
            if visited[i] == 0:
                if not dfs(i):
                    return False
                    
        return True
