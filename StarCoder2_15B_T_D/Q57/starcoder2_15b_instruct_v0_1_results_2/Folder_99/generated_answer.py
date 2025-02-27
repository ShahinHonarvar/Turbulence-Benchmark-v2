import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Takes a two-dimensional numpy matrix of integers and returns a list of all
    submatrices such that the sum of all integers in each submatrix equals -185.
    If no such submatrix is found, returns an empty list.
    """
    num_rows, num_cols = matrix.shape
    submatrices = []
    for row_start in range(num_rows):
        for row_end in range(row_start + 1, num_rows + 1):
            for col_start in range(num_cols):
                for col_end in range(col_start + 1, num_cols + 1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if submatrix.sum() == -185:
                        submatrices.append(submatrix)
    return submatrices