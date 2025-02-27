def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 29 and i <= 93 and (num % 2 != 0)]