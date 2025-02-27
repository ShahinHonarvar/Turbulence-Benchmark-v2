def sum_odd_ints_inclusive(numbers):
    return sum((x for i, x in enumerate(numbers, start=1) if 19 <= i <= 92 and x % 2 != 0))