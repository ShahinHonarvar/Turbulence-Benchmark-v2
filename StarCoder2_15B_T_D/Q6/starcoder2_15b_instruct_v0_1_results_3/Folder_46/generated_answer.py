def all_neg_ints_exclusive(lst):
    res = []
    for i, num in enumerate(lst):
        if num < 0 and 20 <= i < 43:
            res.append(num)
    return res