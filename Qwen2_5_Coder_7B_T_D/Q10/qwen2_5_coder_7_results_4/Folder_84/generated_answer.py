def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if 50 < i < 92 and num % 2 != 0]