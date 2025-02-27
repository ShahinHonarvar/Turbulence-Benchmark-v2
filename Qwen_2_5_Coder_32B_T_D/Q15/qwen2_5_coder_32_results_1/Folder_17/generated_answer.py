def sum_odd_ints_inclusive(numbers):
    return sum((num for idx, num in enumerate(numbers) if idx >= 62 and idx <= 78 and (num % 2 != 0)))