import numpy as np

def submatrix_with_particular_sum(matrix):

    def kadane(matrix, rows, cols, target_sum):
        for left in range(rows):
            temp_sum = 0
            for right in range(left, rows):
                i = left
                row_sum = 0
                for j in range(left, right + 1):
                    row_sum += matrix[i][j]
                    if row_sum == target_sum:
                        yield np.copy(matrix[i:i + 1, left:right + 1])
                    if temp_sum + row_sum < target_sum:
                        temp_sum = temp_sum + row_sum
                        i += 1
                    else:
                        temp_sum = row_sum

    def depth_first_search(matrix, row_start, target_sum, row_len, submatrices):
        for i in range(row_start, matrix.shape[0] - row_len + 1):
            for submatrix in kadane(matrix[i:i + row_len], row_len, matrix.shape[1], target_sum):
                submatrices.append(submatrix)
    submatrices = []
    for row_len in range(1, min(matrix.shape) + 1):
        depth_first_search(matrix, 0, -15, row_len, submatrices)
    return submatrices