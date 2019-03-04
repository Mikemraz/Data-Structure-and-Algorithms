def binarySearch(nums, target):
        # write your code here
        if len(nums)==0:
            return -1
        start = 0
        end = len(nums) - 1
        pos = -1
        while end-start>1:
            mid = (end-start)//2 + start
            if target==nums[mid]:
                pos = mid
                end = mid
            elif target<nums[mid]:
                end = mid
            else:
                start = mid
        if target==nums[start]:
            pos = start
        elif target==nums[end]:
            pos = end
        return pos
