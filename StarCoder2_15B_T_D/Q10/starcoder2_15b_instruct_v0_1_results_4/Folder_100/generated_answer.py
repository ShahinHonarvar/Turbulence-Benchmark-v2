def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 22 and i < 24 and (num % 2 == 1)]