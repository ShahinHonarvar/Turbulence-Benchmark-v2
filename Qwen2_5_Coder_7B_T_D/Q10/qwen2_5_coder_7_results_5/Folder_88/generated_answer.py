def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if 2 < i < 8 and num % 2 != 0]