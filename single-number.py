class Solution:
    '''
    数据前提：重复次数为偶数，且出现一次的数字只有一个
    '''
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for i in nums:
            res=res^i
        return res
        