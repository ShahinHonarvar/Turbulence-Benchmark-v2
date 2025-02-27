def sum_even_ints_inclusive(int_list):
    return sum((n for i, n in enumerate(int_list[33:37]) if n % 2 == 0))