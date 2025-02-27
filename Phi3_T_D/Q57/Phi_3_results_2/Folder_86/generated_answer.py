def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(i, rows):
            for k in range(cols):
                for l in range(k, cols):
                    submatrix_sum = sum((matrix[x][y] for x in range(i, j + 1) for y in range(k, l + 1)))
                    if submatrix_sum == -394:
                        result.append(matrix[i:j + 1, k:l + 1])
    return result