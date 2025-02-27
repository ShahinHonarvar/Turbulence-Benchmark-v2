def all_neg_ints_inclusive(arr):
    res = []
    for i in range(639, 976):
        if arr[i] < 0:
            res.append(arr[i])
    return res