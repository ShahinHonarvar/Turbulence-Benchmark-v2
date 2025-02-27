import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(n, height, width, val=16):
        if height * width < val:
            return 0
        if height == 1 and width == 1:
            return 1 if matrix[0][0] == val else 0
        count = 0
        for h in range(1, height + 1):
            offset = h - 1
            for w in range(1, width + 1):
                offset += w - 1
                right_val = sum((matrix[offset:offset + h][k][w - 1 if w == 1 else w - 2] for k in range(h)))
                if right_val == val:
                    count += h * (width - w + 1)
        return count
    rows, cols = matrix.shape
    return count_submatrices(rows, rows, cols)