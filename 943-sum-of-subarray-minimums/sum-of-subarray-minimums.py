class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        # Pad with negative infinity to clear the stack at the end
        arr = [float('-inf')] + arr + [float('-inf')]
        stack = []
        total_sum = 0
        
        for i, val in enumerate(arr):
            # Maintain a strictly increasing stack
            while stack and arr[stack[-1]] > val:
                mid = stack.pop()
                left = stack[-1]
                right = i
                
                # Count valid subarrays where arr[mid] is the minimum
                count = (mid - left) * (right - mid)
                total_sum += arr[mid] * count
                
            stack.append(i)
            
        return total_sum % MOD
