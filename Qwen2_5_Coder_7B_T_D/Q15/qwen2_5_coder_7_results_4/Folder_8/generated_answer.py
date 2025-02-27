def sum_odd_ints_inclusive(numbers):
    return sum((x for i, x in enumerate(numbers) if i == 23 and x % 2 == 1))