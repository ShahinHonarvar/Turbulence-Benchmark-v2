def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[:7] if i % -5 == 0 or i % -6 == 0))