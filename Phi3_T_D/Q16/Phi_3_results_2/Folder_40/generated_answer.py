def sum_even_ints_inclusive(int_list):
    return sum((n for n in int_list[:3] if n % 2 == 0))