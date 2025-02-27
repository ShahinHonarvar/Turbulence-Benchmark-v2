def sum_odd_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers) if 82 <= i <= 86 and num % 2 != 0))