def all_neg_ints_inclusive(lst):
    result = []
    for x in lst:
        if x < 0:
            result.append(x)
    return result