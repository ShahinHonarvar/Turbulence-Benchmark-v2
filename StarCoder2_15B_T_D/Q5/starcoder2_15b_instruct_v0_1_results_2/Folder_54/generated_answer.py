def all_neg_ints_inclusive(ints):
    result = []
    for i, num in enumerate(ints):
        if num < 0 and 34 <= i <= 55:
            result.append(num)
    return result