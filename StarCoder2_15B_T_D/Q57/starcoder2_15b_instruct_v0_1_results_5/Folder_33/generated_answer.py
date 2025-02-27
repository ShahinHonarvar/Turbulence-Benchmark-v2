from itertools import combinations

def submatrix_with_particular_sum(matrix):
    """
    Finds all submatrices of the given matrix such that the sum of all integers in each submatrix equals -811.
    """
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix = [row[j:l + 1] for row in matrix[i:k + 1]]
                    if sum((sum(x) for x in submatrix)) == -811:
                        submatrices.append(submatrix)
    return submatrices