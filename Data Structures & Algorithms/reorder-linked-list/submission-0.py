# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow_p, fast_p = head, head.next
        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        # reverse second half of list
        second = slow_p.next
        prev = slow_p.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # merge first and second halfs
        first, second  = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        