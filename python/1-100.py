class Solution(object):
    #1
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        M = {}
        for i, n in enumerate(nums):
            M[n] = i
        for i, n in enumerate(nums):
            if M.get(target - n) and M[target - n] != i:
                return [i, M[target - n]]

    #2
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

    #7
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag, x = x <= 0, str(abs(x))
        re = int(x[::-1]) if flag == 0 else -int(x[::-1])
        return re if -2147483648< re <2147483647 else 0

    #8
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        flag, sign = False, 1
        numMap = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        signMap = ['+', '-']
        spaceMap = [' ']
        r = 0
        for s in str:
            if s not in numMap + signMap + spaceMap:
                break
            if flag == True and s not in numMap:
                break
            if r == 0 and s in signMap and flag == False:
                sign = (1 if(s == '+') else -1)
                flag = True
            if s in numMap:
                r = 10 * r + int(s)
                flag = True
        
        r = r * sign
        if r > 2147483647:
            return 2147483647
        if r <-2147483648:
            return -2147483648
        return r

    #9
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        return x == x[::-1]

    #11
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        re, i, j = 0, 0, len(height) - 1
        while(i < j):
            re = max(re, (j - i) * min(height[i], height[j]))
            (i, j) = (i + 1, j) if  height[i]<=height[j] else (i, j - 1)
        return re

    #13
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        r = r + s.count('I')
        r = r + 5 * s.count('V')
        r = r + 10 * s.count('X')
        r = r + 50 * s.count('L')
        r = r + 100 * s.count('C')
        r = r + 500 * s.count('D')
        r = r + 1000 * s.count('M')
        if 'IV' in s or 'IX' in s:
            r = r - 2
        if 'XL' in s or 'XC' in s:
            r = r - 20
        if 'CD' in s or 'CM' in s:
            r = r - 200
        return r

    #55
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        curMax = 0
        for i, n in enumerate(nums):
            if i > curMax:
                return False
            curMax = max(curMax, i + n)
        return True