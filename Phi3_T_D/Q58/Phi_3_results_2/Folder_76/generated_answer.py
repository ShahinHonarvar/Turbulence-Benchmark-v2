import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    height, width = matrix.shape
    count = 0
    for y1 in range(height):
        for x1 in range(width):
            for h in range(height - y1):
                for w in range(width - x1):
                    submatrix = matrix[y1:y1 + h + 1, x1:x1 + w + 1]
                    if np.full(submatrix.shape, 159, dtype=np.int8).sum() == submatrix.size:
                        count += 1
    return count