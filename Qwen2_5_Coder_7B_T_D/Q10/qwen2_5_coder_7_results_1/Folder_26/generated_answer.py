def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 44 and i < 78 and (num % 2 != 0)]