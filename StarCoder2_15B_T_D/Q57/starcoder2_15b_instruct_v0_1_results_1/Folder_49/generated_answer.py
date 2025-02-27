def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix = [row[j:l + 1] for row in matrix[i:k + 1]]
                    if sum((sum(x) for x in submatrix)) == -42:
                        result.append(submatrix)
    return result