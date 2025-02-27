def sum_odd_ints_inclusive(int_list):
    return sum((x for x in int_list[2:7] if x % 2 != 0))