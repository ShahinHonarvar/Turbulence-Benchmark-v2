def all_neg_ints_inclusive(lst):
    result = []
    for i, num in enumerate(lst):
        if num < 0 and 639 <= i <= 975:
            result.append(num)
    return result