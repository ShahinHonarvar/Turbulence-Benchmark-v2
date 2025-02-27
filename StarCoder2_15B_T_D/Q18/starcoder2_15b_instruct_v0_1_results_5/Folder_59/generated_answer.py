def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[:9] if i % -3 == 0 or i % 8 == 0))