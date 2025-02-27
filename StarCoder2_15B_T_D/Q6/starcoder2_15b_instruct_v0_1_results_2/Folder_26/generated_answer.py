def all_neg_ints_exclusive(integers):
    neg_ints = []
    for i, num in enumerate(integers):
        if num < 0 and 44 < i < 78:
            neg_ints.append(num)
    return neg_ints