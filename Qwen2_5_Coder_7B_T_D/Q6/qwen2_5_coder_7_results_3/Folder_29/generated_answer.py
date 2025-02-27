def all_neg_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if 48 < i < 76 and num < 0]