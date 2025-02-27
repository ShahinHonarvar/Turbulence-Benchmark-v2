def all_neg_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if 1 < i < 2 and num < 0]