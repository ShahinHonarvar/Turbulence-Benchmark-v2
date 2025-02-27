def sum_odd_ints_inclusive(numbers):
    return sum((x for i, x in enumerate(numbers) if 64 <= i <= 66 and x % 2 != 0))