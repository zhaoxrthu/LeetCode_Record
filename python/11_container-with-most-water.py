class Solution(object):
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