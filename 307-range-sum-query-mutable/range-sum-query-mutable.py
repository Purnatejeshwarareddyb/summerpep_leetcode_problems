class NumArray:

    def __init__(self, nums: list[int]):
        """
        Initializes the data structure with the input array.
        Time Complexity: O(n log n) or O(n) if optimized.
        """
        self.nums = nums
        self.n = len(nums)
        # Fenwick Tree is 1-indexed, so we allocate size n + 1
        self.tree = [0] * (self.n + 1)
        
        # Build the tree using the initial elements
        for i, num in enumerate(nums):
            self._add(i + 1, num)

    def update(self, index: int, val: int) -> None:
        """
        Updates the value at a specific index to 'val'.
        Time Complexity: O(log n)
        """
        # Calculate the difference between the new value and old value
        delta = val - self.nums[index]
        self.nums[index] = val
        # Propagate the delta through the tree
        self._add(index + 1, delta)

    def sumRange(self, left: int, right: int) -> int:
        """
        Returns the sum of elements between indices left and right inclusive.
        Time Complexity: O(log n)
        """
        # Range sum [left, right] is prefix_sum(right) - prefix_sum(left - 1)
        return self._query(right + 1) - self._query(left)

    def _add(self, idx: int, delta: int) -> None:
        """
        Helper method to add 'delta' to the tree at position 'idx' 
        and all its ancestor responsibilities.
        """
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & (-idx)  # Move to the next responsible parent node

    def _query(self, idx: int) -> int:
        """
        Helper method to get the prefix sum from 1 to 'idx'.
        """
        total = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & (-idx)  # Move to the parent node representing the next block
        return total

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)