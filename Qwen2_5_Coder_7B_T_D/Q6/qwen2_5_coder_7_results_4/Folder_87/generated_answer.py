def all_neg_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if 32 < i < 99 and num < 0]