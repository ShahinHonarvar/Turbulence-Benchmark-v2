import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(row, col, target_sum, current_sum, path, result):
        if row > matrix.shape[0] or col > matrix.shape[1]:
            return
        current_sum += matrix[row, col]
        path.append(matrix[row, col])
        if current_sum == target_sum:
            result.append(path.copy())
        if current_sum < target_sum:
            find_submatrices(row + 1, col, target_sum, current_sum, path, result)
            find_submatrices(row, col + 1, target_sum, current_sum, path, result)
        path.pop()

    def get_all_submatrices():
        submatrices = []
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                find_submatrices(i, j, 100, 0, [], submatrices)
        return submatrices
    all_submatrices = get_all_submatrices()
    filtered_submatrices = [submatrix for submatrix in all_submatrices if np.sum(submatrix) == 100]
    return filtered_submatrices