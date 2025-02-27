import numpy as np
import itertools

def all_submatrices(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for row_slice in range(0, rows + 1):
        for col_slice in range(0, cols + 1):
            submatrix = matrix[row_slice:rows + row_slice, col_slice:cols + col_slice]
            if submatrix.size:
                submatrices.append(submatrix)
    return submatrices

def submatrix_with_particular_sum(matrix, target_sum=-42):
    result = []
    for submatrix in all_submatrices(matrix):
        if submatrix.sum() == target_sum:
            result.append(submatrix)
    return result