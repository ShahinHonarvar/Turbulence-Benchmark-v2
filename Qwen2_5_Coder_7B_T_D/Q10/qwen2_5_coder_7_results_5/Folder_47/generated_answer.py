def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if 64 < i < 80 and num % 2 != 0]