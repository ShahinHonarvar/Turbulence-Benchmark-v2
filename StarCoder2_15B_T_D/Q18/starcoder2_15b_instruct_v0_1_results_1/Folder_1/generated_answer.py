def sum_ints_div_by_either_nums(ints):
    return sum((x for x in ints[10:30] if x % -61 == 0 or x % -64 == 0))