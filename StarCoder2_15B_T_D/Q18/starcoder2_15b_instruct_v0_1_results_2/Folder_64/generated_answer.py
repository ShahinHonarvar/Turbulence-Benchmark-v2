def sum_ints_div_by_either_nums(ints):
    return sum((x for x in ints[:4] if x % 11 == 0 or x % -7 == 0))