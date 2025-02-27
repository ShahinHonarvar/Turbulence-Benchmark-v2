import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum, current_sum, row, col, path, result, visited):
        if current_sum == target_sum:
            result.append(path)
            return
        if current_sum > target_sum or row < 0 or col < 0 or (row >= mat.shape[0]) or (col >= mat.shape[1]) or visited[row][col]:
            return
        visited[row][col] = True
        find_submatrices_with_sum(mat, target_sum, current_sum + mat[row][col], row + 1, col, path + [(row, col)], result, visited)
        find_submatrices_with_sum(mat, target_sum, current_sum + mat[row][col], row - 1, col, path + [(row, col)], result, visited)
        find_submatrices_with_sum(mat, target_sum, current_sum + mat[row][col], row, col + 1, path + [(row, col)], result, visited)
        find_submatrices_with_sum(mat, target_sum, current_sum + mat[row][col], row, col - 1, path + [(row, col)], result, visited)
        visited[row][col] = False
    m, n = matrix.shape
    visited = np.zeros((m, n), dtype=bool)
    all_submatrices = []
    for i in range(m):
        for j in range(n):
            result = []
            find_submatrices_with_sum(matrix, 54, 0, i, j, [], result, visited)
            for res in result:
                submatrix = matrix[np.min([r for r, c in res]):np.max([r for r, c in res]) + 1, np.min([c for r, c in res]):np.max([c for r, c in res]) + 1]
                if submatrix.sum() == 54:
                    all_submatrices.append(submatrix)
    return all_submatrices