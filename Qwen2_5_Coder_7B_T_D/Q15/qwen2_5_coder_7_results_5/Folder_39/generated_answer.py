def sum_odd_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers) if 20 <= i <= 30 and num % 2 != 0))