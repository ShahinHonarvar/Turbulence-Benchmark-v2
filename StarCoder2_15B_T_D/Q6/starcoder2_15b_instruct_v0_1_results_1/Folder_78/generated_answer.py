def all_neg_ints_exclusive(ints):
    result = []
    for i, x in enumerate(ints):
        if x < 0 and 20 <= i < 35:
            result.append(x)
    return result