def all_neg_ints_exclusive(numbers):
    result = []
    for i, num in enumerate(numbers):
        if num < 0 and 41 < i < 69:
            result.append(num)
    return result