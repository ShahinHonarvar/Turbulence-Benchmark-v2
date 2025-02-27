def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 0 and i < 8 and (num % 2 != 0)]