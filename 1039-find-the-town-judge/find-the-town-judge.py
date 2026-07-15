class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        trust_scores = [0] * (n + 1)
        for person_a, person_b in trust:
            trust_scores[person_a] -= 1  
            trust_scores[person_b] += 1
        for i in range(1, n + 1):
            if trust_scores[i] == n - 1:
                return i
                
        return -1
