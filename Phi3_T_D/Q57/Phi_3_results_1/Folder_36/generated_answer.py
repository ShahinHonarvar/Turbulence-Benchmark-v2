import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrix_sums(submatrices):
        return [np.sum(sub) for sub in submatrices]

    def get_submatrices(m, n):
        if m <= 0 or n <= 0:
            return [[]]
        if m == 1:
            return [list(matrix[:, :n])]
        if n == 1:
            return [[list(row)] for row in matrix[:m]]
        submatrices = get_submatrices(m - 1, n)
        for submatrix in get_submatrices(m, n - 1):
            submatrices.append(submatrix[:-1])
        return [submatrix + [row[-1]] for submatrix in get_submatrices(m - 1, n - 1) for row in matrix[m - 2:-1]]
    submatrices = []
    height, width = matrix.shape
    for size_y in range(1, height + 1):
        for size_x in range(1, width + 1):
            submatrices_temp = get_submatrices(size_y, size_x)
            submatrix_sums = get_submatrix_sums([np.array(submatrix) for submatrix in submatrices_temp])
            submatrices.extend([submatrix for submatrix, sum in zip(submatrices_temp, submatrix_sums) if sum == -779])
    return submatrices