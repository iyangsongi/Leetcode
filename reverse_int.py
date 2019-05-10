class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        var_str=str(abs(x))
        reverse=''
        for i in range(len(var_str)):
            reverse += var_str[len(var_str) - 1 - i]
        reverse=int(reverse)
        if reverse < -2 ** 31 or reverse > 2 ** 31 - 1: return 0
        if x>0:
            return int(reverse)
        else:
            return -int(reverse)