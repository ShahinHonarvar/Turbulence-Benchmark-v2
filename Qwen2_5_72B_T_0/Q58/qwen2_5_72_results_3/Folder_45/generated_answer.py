import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, n):
        rows, cols = matrix.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                if (i + 1) * (j + 1) == n:
                    if i < rows and j < cols:
                        count += 1
                elif (rows - i) * (cols - j) >= n:
                    current_submatrix_size = 1
                    for x in range(i, rows):
                        for y in range(j, cols):
                            current_submatrix_size += 1
                            if current_submatrix_size == n:
                                count += 1
                                break
                        if current_submatrix_size >= n:
                            break
        return count
    return count_submatrices_of_size(matrix, 28)