import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_sum(matrix, target):
        rows, cols = matrix.shape
        count = 0
        for top in range(rows):
            row_sum = np.zeros(cols)
            for bottom in range(top, rows):
                row_sum += matrix[bottom]
                current_sum = 0
                seen_sums = {0: 1}
                for value in row_sum:
                    current_sum += value
                    if current_sum - target in seen_sums:
                        count += seen_sums[current_sum - target]
                    seen_sums[current_sum] = seen_sums.get(current_sum, 0) + 1
        return count
    target_sum = 159 * 159
    total_count = 0
    for r in range(matrix.shape[0] - 148):
        for c in range(matrix.shape[1] - 148):
            submatrix = matrix[r:r + 159, c:c + 159]
            total_count += count_submatrices_with_sum(submatrix, target_sum)
    return total_count