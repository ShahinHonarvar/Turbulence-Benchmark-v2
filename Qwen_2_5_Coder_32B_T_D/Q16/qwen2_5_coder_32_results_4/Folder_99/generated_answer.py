def sum_even_ints_inclusive(int_list):
    return sum((x for i, x in enumerate(int_list) if 310 <= i <= 370 and x % 2 == 0)) if len(int_list) > 370 else 0