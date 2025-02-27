def all_neg_ints_inclusive(lst):
    neg_ints = []
    for elem in lst:
        if elem < 0:
            neg_ints.append(elem)
    return neg_ints