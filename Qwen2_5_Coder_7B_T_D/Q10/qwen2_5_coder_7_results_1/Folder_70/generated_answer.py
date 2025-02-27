def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 38 and i < 81 and (num % 2 != 0)]