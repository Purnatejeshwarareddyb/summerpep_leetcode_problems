# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        prev_group = dummy

        while True:

            #  Check if k nodes are available
            kth = prev_group
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # Store the next group's starting node
            next_group = kth.next

            # Reverse current k nodes
            prev = next_group
            curr = prev_group.next

            while curr != next_group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            #  Connect reversed group
            temp = prev_group.next
            prev_group.next = kth
            prev_group = temp