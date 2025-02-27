def sum_even_ints_inclusive(numbers):
    return sum((n for n in numbers[:4] if n % 2 == 0))