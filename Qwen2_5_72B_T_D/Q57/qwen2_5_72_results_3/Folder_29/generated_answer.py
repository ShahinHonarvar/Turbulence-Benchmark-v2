import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices(matrix, target_sum, current_sum=0, submatrix=[], results=[]):
        if current_sum == target_sum:
            results.append(np.array(submatrix))
        elif current_sum < target_sum:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    for height in range(1, len(matrix) - i + 1):
                        for width in range(1, len(matrix[0]) - j + 1):
                            new_submatrix = matrix[i:i + height, j:j + width]
                            new_sum = np.sum(new_submatrix)
                            if new_sum <= target_sum:
                                find_submatrices(matrix, target_sum, new_sum, new_submatrix, results)
        return results
    if not isinstance(matrix, np.ndarray):
        matrix = np.array(matrix)
    all_submatrices = find_submatrices(matrix, 84)
    return [sub.tolist() for sub in all_submatrices if np.sum(sub) == 84]