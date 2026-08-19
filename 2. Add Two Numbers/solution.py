# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2  = l2 

        carry = 0

        dummy = ListNode(0)
        temp = dummy

        while temp1 or temp2:

            val1 = temp1.val if temp1 else 0
            val2 = temp2.val if temp2 else 0

            total = val1 + val2 + carry

            carry = total//10
            digit = total%10

            temp.next = ListNode(digit)
            temp = temp.next

            if temp1:
                temp1 = temp1.next
            
            if temp2:
                temp2 = temp2.next

        if carry:
            temp.next = ListNode(carry)

        return dummy.next

        