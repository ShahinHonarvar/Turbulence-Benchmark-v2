def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 42 and i <= 68 and (num % 2 != 0)]