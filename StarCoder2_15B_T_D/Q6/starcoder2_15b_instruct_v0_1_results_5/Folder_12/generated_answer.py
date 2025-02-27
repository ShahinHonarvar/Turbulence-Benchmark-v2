def all_neg_ints_exclusive(lst):
    result = []
    for i in range(23, 45):
        if lst[i] < 0:
            result.append(lst[i])
    return result