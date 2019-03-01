class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if len(A)==0:
            return 0
        start = 0
        end = len(A)-1
        if target<A[start]:
            return 0
        if target>A[end]:
            return end+1
        pos = -1
        while end-start>1:
            mid = (end-start)//2 + start
            if target==A[mid]:
                pos = mid
                return pos
            elif target<A[mid]:
                end = mid
            else:
                start = mid
        if target==A[start]:
            pos = start
        if A[start]<target<=A[end]:
            pos = end
        return pos
