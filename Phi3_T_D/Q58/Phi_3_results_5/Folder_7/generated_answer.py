import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    rows, cols = matrix.shape
    count = 0
    for sr in range(rows):
        for sc in range(cols):
            for hr in range(rows - sr):
                for hc in range(cols - sc):
                    submatrix = matrix[sr:sr + hr + 1, sc:sc + hc + 1]
                    if submatrix.size == 121:
                        count += 1
    return count