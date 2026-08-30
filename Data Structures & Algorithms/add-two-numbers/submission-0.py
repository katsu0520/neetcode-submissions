# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = ListNode()
        writer = result_head
        carry = 0
        while l1 or l2 or carry:
            if l1:
                v1 = l1.val
            else:
                v1 = 0
            if l2:
                v2 = l2.val
            else:
                v2 = 0
            total = v1 + v2 + carry
            carry = total//10
            val = total%10
            writer.next = ListNode(val)
            writer = writer.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result_head.next
            

            

        