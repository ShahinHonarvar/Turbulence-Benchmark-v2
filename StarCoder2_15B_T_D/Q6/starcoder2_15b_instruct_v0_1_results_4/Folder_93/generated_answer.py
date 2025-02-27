def all_neg_ints_exclusive(lst):
    result = []
    for i, num in enumerate(lst):
        if i >= 19 and i < 94 and (num < 0):
            result.append(num)
    return result