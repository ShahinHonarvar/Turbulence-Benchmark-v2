import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(row, col, target):
        for top in range(row + 1):
            for left in range(col + 1):
                for bottom in range(top + 1, row + 2):
                    for right in range(left + 1, col + 2):
                        submatrix_sum = np.sum(matrix[top:bottom, left:right])
                        if submatrix_sum == target:
                            submatrices.append(matrix[top:bottom, left:right])
    submatrices = []
    target_sum = 94
    rows, cols = matrix.shape
    find_submatrices(rows, cols, target_sum)
    return submatrices