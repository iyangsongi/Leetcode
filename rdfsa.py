class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思路:邻位比较，相同移除不相同加一
        """
        i=0
        while nums:
            if i==(len(nums)-1):return i+1
            if nums[i]==nums[i+1]:
                nums.pop(i+1)
            else:
                i=i+1