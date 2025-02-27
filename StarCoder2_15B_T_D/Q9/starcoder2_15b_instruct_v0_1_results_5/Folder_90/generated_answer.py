def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 262 and i <= 746 and (num % 2 == 1)]