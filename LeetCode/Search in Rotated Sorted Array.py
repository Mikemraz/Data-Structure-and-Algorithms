class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if len(A)==0:
            return -1
        start = 0
        end = len(A) - 1
        while end-start>1:
            mid = (end-start)//2 + start
            if target == A[mid]:
                return mid
            if target>A[-1]:
                if A[-1]<A[mid]<target:
                    start = mid
                else:
                    end = mid
            else:
                if target<A[mid]<A[-1]:
                    end = mid
                else:
                    start = mid
        if target==A[start]:
            return start
        if target==A[end]:
            return end
        return -1
