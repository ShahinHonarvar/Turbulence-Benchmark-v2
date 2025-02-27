def submatrix_with_particular_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = [row[j:l + 1] for row in matrix[i:k + 1]]
                    if sum((sum(x) for x in submatrix)) == -452:
                        submatrices.append(submatrix)
    return submatrices