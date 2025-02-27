def sum_even_ints_inclusive(numbers):
    return sum((x for i, x in enumerate(numbers) if 37 <= i <= 76 and x % 2 == 0))