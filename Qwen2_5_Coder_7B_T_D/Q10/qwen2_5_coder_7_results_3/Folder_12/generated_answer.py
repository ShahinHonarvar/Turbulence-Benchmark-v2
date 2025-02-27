def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 23 and i < 45 and (num % 2 != 0)]