def sum_ints_div_by_either_nums(ints):
    return sum((x for x in ints[:3] if x % -2 == 0 or x % 3 == 0))