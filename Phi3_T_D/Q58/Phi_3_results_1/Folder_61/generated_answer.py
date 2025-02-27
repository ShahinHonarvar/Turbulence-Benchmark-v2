def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            if row + 2 < rows and col + 2 < cols:
                count += 1
    return count