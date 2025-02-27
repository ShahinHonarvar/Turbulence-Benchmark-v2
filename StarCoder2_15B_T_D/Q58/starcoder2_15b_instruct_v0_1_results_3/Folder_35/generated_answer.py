import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            for i in range(row, len(matrix)):
                for j in range(col, len(matrix[0])):
                    submatrix = matrix[row:i + 1, col:j + 1]
                    if submatrix.size == 111:
                        count += 1
    return count