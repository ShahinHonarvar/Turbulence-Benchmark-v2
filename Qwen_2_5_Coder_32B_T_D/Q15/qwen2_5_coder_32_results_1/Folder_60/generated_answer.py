def sum_odd_ints_inclusive(numbers):
    return sum((num for idx, num in enumerate(numbers) if 75 <= idx <= 85 and num % 2 != 0))