def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if 20 < i < 93 and num % 2 != 0]