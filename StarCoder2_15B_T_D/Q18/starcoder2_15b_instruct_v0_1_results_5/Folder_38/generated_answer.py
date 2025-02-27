def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[10:77] if i % -40 == 0 or i % -12 == 0))