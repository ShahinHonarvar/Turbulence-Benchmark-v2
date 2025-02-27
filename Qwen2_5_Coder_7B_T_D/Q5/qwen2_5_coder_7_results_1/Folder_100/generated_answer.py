def all_neg_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers, start=42) if i <= 68 and num < 0]