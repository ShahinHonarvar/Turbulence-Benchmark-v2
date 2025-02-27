def all_neg_ints_inclusive(lst):
    output = []
    for idx, val in enumerate(lst):
        if val < 0 and 52 <= idx <= 71:
            output.append(val)
    return output