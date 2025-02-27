def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 10 and i <= 66 and (num % 2 != 0)]