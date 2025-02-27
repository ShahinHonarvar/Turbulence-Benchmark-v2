def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, numpy.ndarray):
        raise ValueError('Input should be a numpy array')
    total_rows, total_cols = matrix.shape
    count = 0
    for row_start in range(total_rows):
        for col_start in range(total_cols):
            if matrix[row_start, col_start] == 10:
                count += 1
            size = 1
            while row_start + size <= total_rows and col_start + size <= total_cols:
                submatrix = matrix[row_start:row_start + size + 1, col_start:col_start + size + 1]
                if numpy.sum(submatrix) == 10:
                    count += 1
                size += 1
    return count