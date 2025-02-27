def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 29 and i < 53 and (num % 2 != 0)]