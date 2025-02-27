def sum_even_ints_inclusive(int_list):
    return sum((x for i, x in enumerate(int_list) if 17 <= i <= 78 and x % 2 == 0))