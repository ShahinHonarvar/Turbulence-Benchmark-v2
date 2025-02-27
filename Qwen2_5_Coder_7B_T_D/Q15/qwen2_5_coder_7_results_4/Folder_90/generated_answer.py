def sum_odd_ints_inclusive(numbers):
    return sum((x for i, x in enumerate(numbers) if 262 <= i <= 746 and x % 2 != 0))