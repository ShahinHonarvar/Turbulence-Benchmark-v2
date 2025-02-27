import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(start, target, current_sum, current_submatrix, result):
        if start == matrix.size:
            if current_sum == target:
                result.append(current_submatrix)
            return
        row, col = divmod(start, matrix.shape[1])
        find_submatrices(start + 1, target, current_sum + matrix[row, col], np.append(current_submatrix, matrix[row, col]), result)
        find_submatrices(start + 1, target, current_sum, current_submatrix, result)
    all_submatrices = []
    flat_matrix = matrix.flatten()
    find_submatrices(0, 77, 0, np.array([]), all_submatrices)
    return [submatrix.reshape(-1, matrix.shape[1]) for submatrix in all_submatrices if submatrix.size != 0]