def sum_ints_div_by_either_nums(ints):
    return sum((x for x in ints[:9] if x % -3 == 0 or x % 8 == 0))