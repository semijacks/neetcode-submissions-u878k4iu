# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 is None and list2 is None):
            return None
        
        if list1 is None:
            return list2

        if list2 is None:
            return list1
        

        curr1, curr2 = list1, list2
        dummy = ListNode()
        tail = dummy


        while curr1 and curr2:
            if curr1.val < curr2.val:
                tail.next = curr1
                tail = tail.next
                curr1 = curr1.next
            else:
                tail.next = curr2
                tail = tail.next
                curr2 = curr2.next

        if curr1:
            tail.next = curr1
            
        if curr2:
            tail.next = curr2

        return dummy.next

