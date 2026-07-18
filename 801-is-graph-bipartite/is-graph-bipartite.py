class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        color = [0] * n

        for i in range(n):
            if color[i] != 0:
                continue
            
            color[i] = 1
            queue = [i]
            
            while queue:
                u = queue.pop(0)
                
                for v in graph[u]:
                    if color[v] == 0:
                        color[v] = -color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
                        
        return True
