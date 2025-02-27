def all_neg_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if 10 <= i <= 100 and num < 0]