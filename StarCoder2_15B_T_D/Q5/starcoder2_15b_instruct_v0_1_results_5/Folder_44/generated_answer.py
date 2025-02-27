def all_neg_ints_inclusive(lst):
    result = []
    if len(lst) < 68:
        return result
    for i in range(13, 69):
        if lst[i] < 0:
            result.append(lst[i])
    return result