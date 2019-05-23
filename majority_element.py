class Solution:
    '''
    思路：排序后，因为众数长度大于n/2，中间点必定落在众数区间内
    '''
    def majorityElement(self, nums: List[int]) -> int:
            mid=int(len(nums)/2)
            nums.sort()
            return nums[mid]