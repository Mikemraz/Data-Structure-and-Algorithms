def lastPosition(nums, target):
    # write your code here
    if len(nums)==0:
        return -1
    start = 0
    end = len(nums)-1
    pos = -1

    while end-start>1:
        mid = (end-start)//2 + start
        if target==nums[mid]:
            pos = mid
            start = mid
        elif target<nums[mid]:
            end = mid
        else:
            start = mid
    if nums[start]==target:
        pos = start
    if nums[end]==target:
        pos = end
    return pos

lastPosition([0,1,2,3,4,4,5], 4)
