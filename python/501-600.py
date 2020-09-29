class Solution(object):
    #525
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        M, flag, re = {}, 0, 0
        M[0] = -1
        for i, n in enumerate(nums):
            flag = flag + 1 if n else flag - 1
            if M.get(flag) != None:
                re = max(re, i - M[flag])
            else:
                M[flag] = i
        return re