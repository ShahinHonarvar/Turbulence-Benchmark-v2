def all_odd_ints_inclusive(numbers):
    return [num for i, num in enumerate(numbers) if i % 2 == 1 and 0 <= i <= 6]