import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    count = 0
    rows, cols = matrix.shape
    total_numbers = rows * cols
    if total_numbers < 18:
        return 0
    for rowStart in range(rows):
        for colStart in range(cols):
            for subrowSize in range(1, rows - rowStart + 1):
                for subcolSize in range(1, cols - colStart + 1):
                    submatrix = matrix[rowStart:rowStart + subrowSize, colStart:colStart + subcolSize]
                    if submatrix.size == 18:
                        count += 1
    return count