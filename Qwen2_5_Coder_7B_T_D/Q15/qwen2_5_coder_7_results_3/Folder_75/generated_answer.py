def sum_odd_ints_inclusive(numbers):
    return sum((x for i, x in enumerate(numbers) if i in [56, 57] and x % 2 != 0))