def sum_even_ints_inclusive(numbers):
    return sum((x for i, x in enumerate(numbers) if i <= 10 and x % 2 == 0))