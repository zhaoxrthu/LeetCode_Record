class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head, carry = ListNode(0), 0
        ln = head
        while(l1 or l2):
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            if l1:  l1 = l1.next
            if l2:  l2 = l2.next
            ln.next = ListNode((val1 + val2 + carry)%10)
            carry = (val1 + val2 + carry)//10
            ln = ln.next
        ln.next = ListNode(1) if carry == 1 else None
        return head.next