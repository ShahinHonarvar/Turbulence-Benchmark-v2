def sum_odd_ints_inclusive(int_list):
    return sum((x for i, x in enumerate(int_list) if i >= 17 and i <= 78 and (x % 2 != 0)))