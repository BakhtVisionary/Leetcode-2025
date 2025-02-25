from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers represented as linked lists, where each node contains a single digit.
        Digits are stored in reverse order, and the sum is also returned as a linked list.
        """
        dummy = ListNode()  # Dummy node to simplify list construction
        curr = dummy  # Pointer to track the current node
        carry = 0  # Stores carry from previous sum

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0  # Get value from l1, or 0 if None
            v2 = l2.val if l2 else 0  # Get value from l2, or 0 if None

            # Compute sum and carry
            total = v1 + v2 + carry
            carry = total // 10  # Extract carry for the next addition
            val = total % 10  # Extract the current digit

            # Append new node with calculated value
            curr.next = ListNode(val)

            # Move pointers forward
            curr = curr.next 
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next  # Return the head of the resulting linked list
