def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if i >= 21 and i <= 97 and (num % 2 != 0)]