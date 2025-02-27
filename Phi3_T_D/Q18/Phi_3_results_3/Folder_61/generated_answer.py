def sum_ints_div_by_either_nums(ints):
    return sum((x for x in ints[:7] if x % -5 == 0 or x % -6 == 0))