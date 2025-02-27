def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 3 and i <= 5 and (num % 2 != 0)]