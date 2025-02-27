def sum_odd_ints_inclusive(numbers):
    return sum((num for i, num in enumerate(numbers) if i >= 639 and i <= 975 and (num % 2 != 0)))