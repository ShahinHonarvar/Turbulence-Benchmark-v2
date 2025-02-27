def sum_even_ints_inclusive(int_list):
    return sum((x for i, x in enumerate(int_list) if 8 <= i <= 80 and x % 2 == 0))