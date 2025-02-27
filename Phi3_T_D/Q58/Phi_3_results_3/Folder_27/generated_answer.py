def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 77
    for row_top in range(rows):
        for col_left in range(cols):
            for row_bottom in range(row_top, rows):
                for col_right in range(col_left, cols):
                    submatrix = matrix[row_top:row_bottom + 1, col_left:col_right + 1]
                    if num_integers(submatrix) == n:
                        count += 1
    return count

def num_integers(matrix):
    return np.sum(matrix == 77)