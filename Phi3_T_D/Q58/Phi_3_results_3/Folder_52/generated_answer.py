import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(mat, target_count):
        m, n = mat.shape
        counts = 0
        for i in range(m):
            for j in range(n):
                for new_m in range(i, m):
                    for new_n in range(j, n):
                        submat = mat[i:new_m + 1, j:new_n + 1]
                        if (submat == 0).sum() == target_count:
                            counts += 1
        return counts
    target_submatrix_size = 147
    total_elements = matrix.size
    if total_elements < target_submatrix_size:
        return 0
    return count_submatrices(matrix, target_submatrix_size)