def all_neg_ints_exclusive(lst):
    neg_ints = []
    for i, num in enumerate(lst):
        if num < 0 and 323 < i < 972:
            neg_ints.append(num)
    return neg_ints