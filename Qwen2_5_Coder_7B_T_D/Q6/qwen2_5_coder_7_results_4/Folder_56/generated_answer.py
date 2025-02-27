def all_neg_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 7 and i < 9 and (num < 0)]