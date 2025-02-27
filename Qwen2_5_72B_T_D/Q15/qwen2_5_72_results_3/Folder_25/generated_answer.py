def sum_odd_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers) if 29 <= i <= 93 and num % 2 != 0))