import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def search_submatrix(start_r, start_c, end_r, end_c):
        if end_r <= start_r or end_c <= start_c:
            return
        current_sum = np.sum(matrix[start_r:end_r, start_c:end_c])
        if current_sum == 40:
            result.append(matrix[start_r:end_r, start_c:end_c].copy())
        mid_r, mid_c = ((start_r + end_r) // 2, (start_c + end_c) // 2)
        search_submatrix(start_r, start_c, mid_r, mid_c)
        search_submatrix(start_r, mid_c + 1, mid_r, end_c)
        search_submatrix(mid_r + 1, start_c, end_r, mid_c)
        search_submatrix(mid_r + 1, mid_c + 1, end_r, end_c)
    search_submatrix(0, 0, rows, cols)
    return result