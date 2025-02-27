def sum_odd_ints_inclusive(numbers):
    return sum((x for i, x in enumerate(numbers) if 60 <= i <= 200 and x % 2 != 0))