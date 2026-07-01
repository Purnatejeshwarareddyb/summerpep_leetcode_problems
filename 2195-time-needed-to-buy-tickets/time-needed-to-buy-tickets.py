class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time = 0
        for i in range(len(tickets)):
            # If the person is before or at the target index
            if i <= k:
                time += min(tickets[i], tickets[k])
            # If the person is after the target index
            else:
                time += min(tickets[i], tickets[k] - 1)
        return time
