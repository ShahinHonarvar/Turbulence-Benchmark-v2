def sum_even_ints_inclusive(numbers):
    return sum((x for i, x in enumerate(numbers) if 62 <= i <= 63 and x % 2 == 0))