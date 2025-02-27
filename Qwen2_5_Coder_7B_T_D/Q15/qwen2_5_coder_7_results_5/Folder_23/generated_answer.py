def sum_odd_ints_inclusive(numbers):
    return sum((x for i, x in enumerate(numbers) if 52 <= i <= 71 and x % 2 != 0))