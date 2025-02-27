def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 17 and i <= 78 and (num % 2 == 1)]