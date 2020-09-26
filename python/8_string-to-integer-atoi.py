class Solution(object):
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