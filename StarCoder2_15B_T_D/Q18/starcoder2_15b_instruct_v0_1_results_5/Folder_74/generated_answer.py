def sum_ints_div_by_either_nums(ints):
    return sum((x for x in ints[90:98] if x % 13 == 0 or x % 35 == 0))