def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 19 and i <= 92 and (num % 2 == 1)]