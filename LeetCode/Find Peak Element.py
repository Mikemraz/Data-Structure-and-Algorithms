class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        start = 0
        end = len(A)-1
        while end-start>1:
            mid = (end-start)//2 + start
            if A[mid]>A[mid-1] and A[mid]>A[mid+1]:
                return mid
            elif A[mid]<A[mid+1]:
                start = mid
            elif A[mid]<A[mid-1]:
                end = mid
            
