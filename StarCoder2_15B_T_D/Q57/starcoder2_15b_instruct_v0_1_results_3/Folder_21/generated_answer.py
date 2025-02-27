def submatrix_with_particular_sum(matrix):
    n, m = (len(matrix), len(matrix[0]))
    submatrices = []
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    submatrix = [row[j:l + 1] for row in matrix[i:k + 1]]
                    if sum((sum(x) for x in submatrix)) == -936:
                        submatrices.append(submatrix)
    return submatrices