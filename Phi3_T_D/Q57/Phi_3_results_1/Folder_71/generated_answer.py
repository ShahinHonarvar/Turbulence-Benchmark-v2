import numpy as np

def submatrix_with_particular_sum(matrix):
    total_num = matrix.size
    res = []
    for i in range(total_num):
        for j in range(i, total_num):
            sub = matrix.flat[i:j + 1]
            sub_arr = sub.reshape(-1, sub.shape[0] // sub.shape[1])
            if sub_arr.size > 0:
                for k in range(sub_arr.shape[0]):
                    for l in range(sub_arr.shape[1]):
                        for m in range(k, sub_arr.shape[0]):
                            for n in range(l, sub_arr.shape[1]):
                                submatrix = sub_arr[k:m + 1, l:n + 1]
                                if submatrix.sum() == 69:
                                    res.append(submatrix)
    return res