def sum_even_ints_inclusive(integers):
    even_sum = sum((n for i, n in enumerate(integers) if 10 <= i <= 100 and n % 2 == 0))
    return even_sum