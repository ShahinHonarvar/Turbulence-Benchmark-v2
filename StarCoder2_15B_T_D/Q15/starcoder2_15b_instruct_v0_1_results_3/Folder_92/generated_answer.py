def sum_odd_ints_inclusive(ints_list):
    return sum((x for x in ints_list[1:2] if x % 2 != 0))