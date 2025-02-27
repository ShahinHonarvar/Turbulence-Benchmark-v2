def sum_ints_div_by_either_nums(ints):
    return sum((x for x in ints[:5] if x % 8 == 0 or x % -3 == 0))