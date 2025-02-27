def sum_ints_div_by_either_nums(ints):
    return sum((x for x in ints[29:46] if x % 27 == 0 or x % 81 == 0))