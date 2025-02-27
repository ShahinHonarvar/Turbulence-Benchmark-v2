def submatrix_with_particular_sum(matrix):
    res = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    submat = matrix[i:k, j:l]
                    if submat.sum() == -128:
                        res.append(submat)
    return res