def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 41 and i < 69 and (num % 2 == 1)]