def sum_even_ints_inclusive(int_list):
    return sum((n for i, n in enumerate(int_list[3:6], start=3) if n % 2 == 0))