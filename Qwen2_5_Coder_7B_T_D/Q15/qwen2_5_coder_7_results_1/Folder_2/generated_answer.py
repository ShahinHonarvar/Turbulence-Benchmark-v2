def sum_odd_ints_inclusive(numbers):
    return sum((x for i, x in enumerate(numbers) if 15 <= i <= 39 and x % 2 != 0))