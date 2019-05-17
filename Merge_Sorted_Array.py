class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        #比较nums1与nums2最后实际一位，取大者放在最后生成数组的最后一位，一次向前推进，直至num2比较完成
        while n > 0:
            if m and nums1[m-1] > nums2[n-1]:
                nums1[m+n-1], m, n = nums1[m-1], m-1, n
            else:
                nums1[m+n-1], m, n = nums2[n - 1], m, n-1