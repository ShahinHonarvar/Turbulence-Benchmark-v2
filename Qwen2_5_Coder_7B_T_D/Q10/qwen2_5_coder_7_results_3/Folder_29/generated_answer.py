def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers, start=1) if 48 < i < 77 and num % 2 != 0]