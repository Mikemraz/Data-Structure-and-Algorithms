"""38. Search a 2D Matrix II
Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.

This matrix has the following properties:

Integers in each row are sorted from left to right.
Integers in each column are sorted from up to bottom.
No duplicate integers in each row or column.
Example
Example 1:

Input:
	[[3,4]]
	target=3
Output:1
Example 2:

Input:
    [
      [1, 3, 5, 7],
      [2, 4, 7, 8],
      [3, 5, 9, 10]
    ]
    target = 3
Output:2
Challenge
O(m+n) time and O(1) extra space"""

class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # check if the matrix is empty
        if len(matrix)==0:
            return 0
        # chech if the target is within the value range of this matrix.
        rows = len(matrix) - 1
        columns = len(matrix[0]) - 1
        if target<matrix[0][0] or target>matrix[rows][columns]:
            return 0
        # start from bottom-left element, compare the target value to conner
        # element of assigned row-column pair.
        row = rows
        column = 0
        count = 0
        while row>=0 and column<=columns:
            if target==matrix[row][column]:
                count += 1
                row -= 1
            elif target<matrix[row][column]:
                row -= 1
            else:
                column += 1
        return count
