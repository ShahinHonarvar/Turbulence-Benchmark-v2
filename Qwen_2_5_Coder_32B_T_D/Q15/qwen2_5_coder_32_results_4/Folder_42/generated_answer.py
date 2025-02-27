def sum_odd_ints_inclusive(int_list):
    return sum((x for i, x in enumerate(int_list) if 29 <= i <= 79 and x % 2 != 0))