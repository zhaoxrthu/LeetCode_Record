class Solution(object):
    #406
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        class cmp():
            def __init__(self, array):
                self.v = array
            def __gt__(self, b):
                return self.v[1] > b.v[1] or self.v[1] == b.v[1] and self.v[0] > b.v[0]
        people, re = sorted(people, key = cmp), []
        for p in people:
            h, k, kcount, flag = p[0], p[1], 0, False
            for i in xrange(len(re)):
                if re[i][0] >= h:    kcount = kcount + 1
                if kcount > k:
                    re, flag = re[0:i] + [p] + re[i:], True
                    break
            if flag == False:   re = re + [p]
        return re

    #477
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        re, l = 0, len(nums)
        M = [0 for _ in xrange(36)]
        for n in nums:
            i = 0
            while(n):
                M[i] = M[i] + (n & 1)
                n, i = n >> 1, i + 1
        for m in M:
            if m:
                re = re + m * (l - m)
        return re

    #459    
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        for i in xrange(1, (l >> 1) + 1):
            p, q = l // i, l % i
            if q == 0 and s[0:i]*p == s:
                return True
        return False

    #495
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        re, finishT = 0, 0
        for i, t in enumerate(timeSeries):
            re = re + duration if t >= finishT else re + t - timeSeries[i-1]
            finishT = t + duration
        return re