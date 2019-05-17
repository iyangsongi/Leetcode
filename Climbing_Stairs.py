class Solution(object):
	"""
	使用动态规划原理，当前步骤由上一步结果获得，并存储结果用于重复计算
	"""
    def __init__(self):
        self.map = {1:1, 2:2}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """      
        if not n in self.map: self.map[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.map[n]