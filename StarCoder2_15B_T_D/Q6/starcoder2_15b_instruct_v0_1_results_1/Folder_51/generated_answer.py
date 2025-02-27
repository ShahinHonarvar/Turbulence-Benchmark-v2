def all_neg_ints_exclusive(ints):
    result = []
    for i, val in enumerate(ints):
        if val < 0 and 6 <= i < 9:
            result.append(val)
    return result