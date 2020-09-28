class Solution(object):
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