class Solution(object):
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