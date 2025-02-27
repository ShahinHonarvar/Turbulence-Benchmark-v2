def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i > 20 and i < 51 and (num % 2 != 0)]