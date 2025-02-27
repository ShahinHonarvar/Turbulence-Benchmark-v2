def all_neg_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i in range(1, 7) and num < 0]