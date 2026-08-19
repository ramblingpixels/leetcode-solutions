# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        temp = head
        count = 0

        while temp is not None:
            count += 1
            temp = temp.next

        if count == 1:
            head = None
            return head

        i = 1
        temp = head
        prev = None

        while i <= (count - n):
            prev = temp
            temp = temp.next
            i += 1
        
        if prev == None:
            return head.next

        prev.next = temp.next
        temp.next = None

        return head
