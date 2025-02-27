import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_sum_zero(matrix, rows, cols):
        result = []
        for start_row in range(rows):
            for end_row in range(start_row, rows):
                prefix_sums = [0] * (cols + 1)
                for col in range(cols):
                    prefix_sums[col + 1] = prefix_sums[col] + sum(matrix[start_row:end_row + 1, col])
                submatrix_sums = {}
                for i in range(cols + 1):
                    if prefix_sums[i] in submatrix_sums:
                        for left in submatrix_sums[prefix_sums[i]]:
                            result.append(matrix[start_row:end_row + 1, left:i])
                        submatrix_sums[prefix_sums[i]].append(i)
                    else:
                        submatrix_sums[prefix_sums[i]] = [i]
        return result
    matrix = np.array(matrix)
    rows, cols = matrix.shape
    return find_submatrices_sum_zero(matrix, rows, cols)