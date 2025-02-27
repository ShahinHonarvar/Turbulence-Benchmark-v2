def sum_even_ints_inclusive(int_list):
    return sum((x for i, x in enumerate(int_list) if i >= 262 and i <= 746 and (x % 2 == 0)))