def all_neg_ints_exclusive(numbers):
    result = []
    for i, num in enumerate(numbers):
        if num < 0 and 44 < i < 67:
            result.append(num)
    return result