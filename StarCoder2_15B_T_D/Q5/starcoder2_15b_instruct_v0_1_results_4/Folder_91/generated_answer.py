def all_neg_ints_inclusive(lst):
    result = []
    for i, x in enumerate(lst):
        if x < 0 and i >= 0 and (i <= 5):
            result.append(x)
    return result