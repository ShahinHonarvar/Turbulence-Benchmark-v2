def sum_odd_ints_inclusive(int_list):
    return sum((x for i, x in enumerate(int_list[:3]) if x % 2 != 0))