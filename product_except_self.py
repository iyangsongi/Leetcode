class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return nums
        A = [1] * len(nums)
        B = [1] * len(nums)
        for i in range(1,len(nums)):
            A[i] = A[i-1] * nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            B[i] = B[i+1] * nums[i+1]
        
        return [A[i]*B[i] for i in range(len(nums))]