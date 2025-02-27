def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers, start=1) if i > 11 and i < 76 and (num % 2 != 0)]