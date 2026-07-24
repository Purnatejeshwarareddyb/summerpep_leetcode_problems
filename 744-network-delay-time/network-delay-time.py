class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
            
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        visited = [False] * (n + 1)
        
        for _ in range(n):
            curr_node = -1
            curr_dist = float('inf')
            for i in range(1, n + 1):
                if not visited[i] and dist[i] < curr_dist:
                    curr_dist = dist[i]
                    curr_node = i
            
            if curr_node == -1 or curr_dist == float('inf'):
                break
                
            visited[curr_node] = True
            
            for neighbor, weight in graph[curr_node]:
                if dist[curr_node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[curr_node] + weight
                    
        max_time = 0
        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                return -1
            if dist[i] > max_time:
                max_time = dist[i]
                
        return max_time
