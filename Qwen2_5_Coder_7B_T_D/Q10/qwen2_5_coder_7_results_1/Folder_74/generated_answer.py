def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 13 and i < 70 and (num % 2 != 0)]