def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 36 and i < 52 and (num % 2 != 0)]