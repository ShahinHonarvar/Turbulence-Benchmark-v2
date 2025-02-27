import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(row_start, col_start, current_sum, submatrix):
        submatrices = []
        for i in range(row_start, len(matrix)):
            for j in range(col_start, len(matrix[0])):
                current_sum[i][j] = 0 if i == row_start and j == col_start else current_sum[i][j - 1]
                current_sum[i][j] += matrix[i][j]
                for k in range(row_start, i + 1):
                    if current_sum[i][j] - current_sum[k][j] == 40:
                        submatrix.append(matrix[k:i + 1, col_start:j + 1])
        return submatrices
    current_sum = np.zeros((len(matrix), len(matrix[0]) + 1), dtype=int)
    all_submatrices = []
    for row_start in range(len(matrix)):
        for col_start in range(len(matrix[0])):
            if row_start > 0:
                current_sum[row_start] = current_sum[row_start - 1]
                current_sum[row_start, :-1] = current_sum[row_start - 1, :-1]
            all_submatrices.extend(find_submatrices(row_start, col_start, current_sum, []))
    return all_submatrices