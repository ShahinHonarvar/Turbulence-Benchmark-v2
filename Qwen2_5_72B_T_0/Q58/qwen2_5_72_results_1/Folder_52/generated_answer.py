import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        count = 0
        rows, cols = mat.shape
        for i in range(rows):
            for j in range(cols):
                if (i + 1) * (j + 1) == n:
                    count += 1
                elif (rows - i) * (j + 1) < n or (cols - j) * (i + 1) < n:
                    continue
                else:
                    submat = mat[i:rows, j:cols]
                    if submat.size >= n:
                        count += np.sum([sub.size == n for sub in [submat[:k, :l] for k in range(1, submat.shape[0] + 1) for l in range(1, submat.shape[1] + 1) if k * l == n]])
        return count
    return count_submatrices_with_n_elements(matrix, 147)