def sum_even_ints_inclusive(numbers):
    return sum((x for i, x in enumerate(numbers) if 30 <= i <= 87 and x % 2 == 0))