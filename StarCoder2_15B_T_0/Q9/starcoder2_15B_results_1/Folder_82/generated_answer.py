def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 20 and i <= 200 and (num % 2 == 1)]