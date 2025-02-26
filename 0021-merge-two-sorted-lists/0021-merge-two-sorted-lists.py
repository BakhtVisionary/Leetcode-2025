# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()  # Dummy node
        output = curr  # Pointer to start of the merged list

        while list1 and list2:  # Corrected condition
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            
            curr = curr.next  # Move the pointer forward

        if list1:
            curr.next = list1
        if list2:
            curr.next = list2

        return output.next  
