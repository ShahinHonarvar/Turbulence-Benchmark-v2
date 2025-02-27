def all_neg_ints_exclusive(numbers):
    return [num for index, num in enumerate(numbers) if 0 < index < 5 and num < 0]