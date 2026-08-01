class Solution:
  def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    memo = {}
    def check(i, j):
      if i == len(text1) or j == len(text2):
        return 0
      if (i, j) in memo:
        return memo[(i, j)]

      if text1[i] == text2[j]:
        memo[(i, j)] = 1 + check(i + 1, j + 1)
      else:
        skip_text1 = check(i + 1, j)
        skip_text2 = check(i, j + 1)
        memo[(i, j)] = max(skip_text1, skip_text2)
      return memo[(i, j)]
    return check(0, 0)
