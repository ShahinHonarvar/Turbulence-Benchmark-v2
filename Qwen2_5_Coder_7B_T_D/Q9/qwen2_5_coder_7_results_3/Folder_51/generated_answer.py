def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers, start=1) if 1 <= i <= 8 and num % 2 != 0]