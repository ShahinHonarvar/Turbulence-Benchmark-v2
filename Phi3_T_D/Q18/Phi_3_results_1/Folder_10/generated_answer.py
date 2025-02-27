def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[32:99 + 1] if i % -11 == 0 or i % -15 == 0))