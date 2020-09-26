class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag, x = x <= 0, str(abs(x))
        re = int(x[::-1]) if flag == 0 else -int(x[::-1])
        return re if -2147483648< re <2147483647 else 0