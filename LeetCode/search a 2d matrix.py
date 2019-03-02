def searchMatrix(matrix, target):
    # write your code here
    if len(matrix)==0:
        return False
    row_number = len(matrix)
    column_number = len(matrix[0])
    if target<matrix[0][0]:
        return False
    if target>matrix[row_number-1][column_number-1]:
        return False
    # compare first element of each row and return a row index where target resides.
    start_row = 0
    end_row = row_number - 1
    target_row = -1
    while end_row-start_row>1:
        mid = (end_row-start_row)//2 + start_row
        if target==matrix[mid][0]:
            return True
        elif target<matrix[mid][0]:
            end_row = mid
        else:
            start_row = mid
    if target==matrix[start_row][0]:
        return True
    elif matrix[start_row][0]<target<matrix[end_row][0]:
        target_row = start_row
    elif target==matrix[end_row][0]:
        return True
    elif target>matrix[end_row][0]:
        target_row = end_row
    # then search in target row
    start_column = 0
    end_column = column_number - 1
    while end_column-start_column>1:
        mid = (end_column-start_column)//2 + start_column
        if target==matrix[target_row][mid]:
            return True
        elif target<matrix[target_row][mid]:
            end_column = mid
        else:
            start_column = mid
    if target==matrix[target_row][start_column]:
        return True
    if target==matrix[target_row][end_column]:
        return True
    return False

if __name__=="__main__":
    A = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    print(searchMatrix(A, 7))
