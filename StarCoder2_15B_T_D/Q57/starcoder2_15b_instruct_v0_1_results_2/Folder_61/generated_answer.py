import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Finds all submatrices of the given matrix such that the sum of all integers in each submatrix equals 8.
    """

    def submatrix_sum(submatrix):
        """
        Calculates the sum of all integers in a submatrix.
        """
        return np.sum(submatrix)

    def generate_submatrices(matrix):
        """
        Generates all submatrices of the given matrix.
        """
        n, m = matrix.shape
        for i in range(n):
            for j in range(m):
                for k in range(i, n):
                    for l in range(j, m):
                        yield matrix[i:k + 1, j:l + 1]
    submatrices = generate_submatrices(matrix)
    return [submatrix for submatrix in submatrices if submatrix_sum(submatrix) == 8]