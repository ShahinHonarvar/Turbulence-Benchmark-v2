def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[1:5] if i % 4 == 0 or i % -6 == 0))