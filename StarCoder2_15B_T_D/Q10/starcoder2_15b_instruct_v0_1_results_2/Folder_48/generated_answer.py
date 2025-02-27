def all_odd_ints_exclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 385 and i < 999 and (num % 2 == 1)]