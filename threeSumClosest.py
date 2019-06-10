class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:  
        res=float("inf")
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if cur_sum == target:return target
                if abs(res-target) > abs(cur_sum-target):
                    res = cur_sum
                if cur_sum > target:
                    right -= 1
                elif cur_sum < target:
                    left += 1
        return res