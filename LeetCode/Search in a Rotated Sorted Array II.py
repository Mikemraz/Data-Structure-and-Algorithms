"""Description
Follow up for Search in Rotated Sorted Array:

What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

Have you met this question in a real interview?
Example
Example 1:

Input:
[]
1
Output:
false
Example 2:

Input:
[3,4,4,5,7,0,1,2]
4
Output:
true
"""
class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean
    """
    # This quiz is not much different from the quiz of searching the minimum
    # in a roated sorted array II.
    def search(self, A, target):
        # write your code here
        if len(A)==0:
            return False
        while len(A)>=2 and A[0]==A[-1]:
            A.pop(-1)

        head = 0
        tail = len(A) - 1
        while tail-head>1:
            mid = (tail-head)//2 + head
            if target==A[mid]:
                return True
            elif A[mid]<=A[-1]:
                if A[mid]<=target<=A[-1]:
                    head = mid
                else:
                    tail = mid
            else:
                if A[-1]<target<=A[mid]:
                    tail = mid
                else:
                    head = mid
        if target==A[head] or target==A[tail]:
            return True
        return False
