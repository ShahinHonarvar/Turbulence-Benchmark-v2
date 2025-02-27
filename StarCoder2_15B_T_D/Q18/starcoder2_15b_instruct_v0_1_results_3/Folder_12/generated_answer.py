def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[35:65] if i % -30 == 0 or i % -95 == 0))