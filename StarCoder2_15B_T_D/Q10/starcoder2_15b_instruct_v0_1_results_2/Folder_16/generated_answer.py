def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 85 and i < 90 and (num % 2 == 1)]