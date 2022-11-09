## LeetCode Problem
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        current = dummyHead
        carry = 0
        while l1 or l2 or carry != 0:
            value_one = l1.val if l1 else 0
            value_two = l2.val if l2 else 0
            sum = value_one + value_two + carry
            if carry == 1:
                carry = 0
            if sum > 9:
                sum = sum % 10
                carry = 1
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            newNode = ListNode(sum)
            current.next = newNode
            current = current.next

        return dummyHead.next
