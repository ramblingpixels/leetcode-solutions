# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        stack1 = []
        stack2 = []
        temp2 = l2
        num1 = 0
        num2 = 0
        p1=1
        p2=1

        while temp1:
            stack1.append(temp1)
            temp1 = temp1.next
        
        while stack1:
            node = stack1.pop()
            num1 = num1*10 + node.val
            # p1 = p1*10

        while temp2:
            stack2.append(temp2)
            temp2 = temp2.next
        
        while stack2:
            node = stack2.pop()
            num2 = num2*10 + node.val
            # p2 = p2*10

        sum = num1 + num2

        print(num1, num2, sum)

        head = ListNode(sum%10)
        temp = head
        sum = sum // 10

        while sum > 0:
            temp.next = ListNode(sum%10)
            temp = temp.next
            sum = sum//10
        
        return head

        