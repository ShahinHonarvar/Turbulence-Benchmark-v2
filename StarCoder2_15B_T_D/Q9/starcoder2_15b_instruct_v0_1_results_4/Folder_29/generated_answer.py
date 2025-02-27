def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 59 and i <= 97 and (num % 2 == 1)]