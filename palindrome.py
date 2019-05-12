class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        i=0
        while i<=int(len(x)/2):
            if x[i]!=x[len(x)-1-i]:
                return False
            i+=1
        return True