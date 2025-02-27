import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrix_sum(arr, target_sum):
        row, col = arr.shape
        result = []
        for start_row in range(row):
            for start_col in range(col):
                for end_row in range(start_row + 1, row + 1):
                    for end_col in range(start_col + 1, col + 1):
                        submatrix = arr[start_row:end_row, start_col:end_col]
                        if np.sum(submatrix) == target_sum:
                            result.append(submatrix)
        return result
    return find_submatrix_sum(matrix, -10)