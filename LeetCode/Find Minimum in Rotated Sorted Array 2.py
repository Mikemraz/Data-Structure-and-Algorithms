"""
160. Find Minimum in Rotated Sorted Array II
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

Example
Example 1:

Input :[2,1]
Output : 1.
Example 2:

Input :[4,4,5,6,7,0,1,2]
Output : 0.
Notice
The array may contain duplicates.
"""

"""
this quiz is not much different from Find Minimum in Rotated Sorted Array I
except that elements could be duplicates. All we care is that the first element
and last element differs from each other. So to deleting one of them till they
are different is a reasonalbe choice. However, the O(LogN) could degraded to
O(N).
"""
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        while len(nums)>1:
            if nums[0]==nums[-1]:
                nums.pop(-1)
            else:
                break
        head = 0
        tail = len(nums)-1
        while tail-head>1:
            mid = (tail-head)//2 + head
            if nums[mid]<=nums[tail]:
                tail = mid
            else:
                head = mid
        return min(nums[head],nums[tail])
