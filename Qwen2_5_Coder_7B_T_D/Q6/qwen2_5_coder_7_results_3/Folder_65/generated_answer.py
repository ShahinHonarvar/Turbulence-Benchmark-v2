def all_neg_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if 42 < i < 87 and num < 0]