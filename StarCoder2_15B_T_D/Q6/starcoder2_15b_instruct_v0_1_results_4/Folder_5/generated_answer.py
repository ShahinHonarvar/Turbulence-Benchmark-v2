def all_neg_ints_exclusive(lst):
    result = []
    for i, num in enumerate(lst):
        if num < 0 and 2 < i < 7:
            result.append(num)
    return result