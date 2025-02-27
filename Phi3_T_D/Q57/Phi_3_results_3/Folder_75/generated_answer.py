import numpy as np

def submatrix_with_particular_sum(matrix):

    def _get_submatrix(mat, top, left, bottom, right):
        return mat[top:bottom, left:right]

    def _find_submatrices(mat, t, l, b, r, target, path, paths):
        if t == b and l == r:
            path_sum = np.sum(mat[t, l])
            if path_sum == target:
                paths.append([row[l:r + 1].tolist() for row in mat[t:b + 1]])
            return
        if l < r:
            _find_submatrices(mat, t, l + 1, b, r, target, path + [mat[t, l:l + 1]], paths)
        if t < b:
            _find_submatrices(mat, t + 1, l, b, r, target, path + [mat[t + 1:t + 2, l]], paths)
    target_sum = 16
    rows, cols = matrix.shape
    all_submatrices = []
    for row_len in range(1, rows + 1):
        for col_len in range(1, cols + 1):
            for i in range(rows - row_len + 1):
                for j in range(cols - col_len + 1):
                    submat = _get_submatrix(matrix, i, j, i + row_len - 1, j + col_len - 1)
                    _find_submatrices(submat, 0, 0, submat.shape[0] - 1, submat.shape[1] - 1, target_sum, [], all_submatrices)
    return all_submatrices