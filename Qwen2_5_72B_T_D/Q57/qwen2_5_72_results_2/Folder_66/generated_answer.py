import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum, current_sum, row, col, rows, cols, result, path):
        if current_sum == target_sum:
            result.append(path)
            return
        if row >= rows or col >= cols:
            return
        if current_sum + mat[row][col] <= target_sum:
            find_submatrices_with_sum(mat, target_sum, current_sum + mat[row][col], row, col + 1, rows, cols, result, path + [(row, col)])
            find_submatrices_with_sum(mat, target_sum, current_sum + mat[row][col], row + 1, col, rows, cols, result, path + [(row, col)])
        find_submatrices_with_sum(mat, target_sum, current_sum, row, col + 1, rows, cols, result, path)
        find_submatrices_with_sum(mat, target_sum, current_sum, row + 1, col, rows, cols, result, path)

    def get_submatrix_elements(matrix, coordinates):
        submatrix_elements = []
        row_min = min([x[0] for x in coordinates])
        row_max = max([x[0] for x in coordinates])
        col_min = min([x[1] for x in coordinates])
        col_max = max([x[1] for x in coordinates])
        for i in range(row_min, row_max + 1):
            for j in range(col_min, col_max + 1):
                if (i, j) in coordinates:
                    submatrix_elements.append(matrix[i][j])
        return submatrix_elements
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return []
    result = []
    rows, cols = matrix.shape
    find_submatrices_with_sum(matrix, 99, 0, 0, 0, rows, cols, result, [])
    final_result = [get_submatrix_elements(matrix, res) for res in result]
    return final_result