def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 27 and i <= 55 and (num % 2 != 0)]