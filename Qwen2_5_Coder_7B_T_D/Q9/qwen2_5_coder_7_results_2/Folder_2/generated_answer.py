def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 15 and i <= 39 and (num % 2 != 0)]