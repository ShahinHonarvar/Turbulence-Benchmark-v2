def all_neg_ints_exclusive(lst):
    result = []
    for i, num in enumerate(lst):
        if num < 0 and 38 <= i < 81:
            result.append(num)
    return result