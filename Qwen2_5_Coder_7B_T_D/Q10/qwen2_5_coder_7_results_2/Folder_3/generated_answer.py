def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 78 and i < 93 and (num % 2 != 0)]