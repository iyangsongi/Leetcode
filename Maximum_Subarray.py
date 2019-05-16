class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思路：当前位置与上一位置求最大和，依次遍历，初始操作为num[1]+num[0]的判断
        """
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        return max(nums)