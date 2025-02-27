def all_neg_ints_exclusive(lst):
    result = []
    for i in range(len(lst)):
        if lst[i] < 0 and 38 < i < 52:
            result.append(lst[i])
    return result