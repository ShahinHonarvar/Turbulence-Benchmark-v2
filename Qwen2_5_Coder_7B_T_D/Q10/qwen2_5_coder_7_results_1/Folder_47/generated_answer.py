def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 64 and i < 80 and (num % 2 != 0)]