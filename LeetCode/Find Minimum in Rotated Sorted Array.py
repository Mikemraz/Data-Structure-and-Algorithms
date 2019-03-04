class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if len(nums)==0:
            return 0
        start = 0
        end = len(nums) - 1
        while end-start>1:
            mid = (end-start)//2 + start
            if nums[mid]<=nums[-1]:
                end = mid
            else:
                start = mid
        return nums[start] if nums[start]<nums[end] else nums[end]
