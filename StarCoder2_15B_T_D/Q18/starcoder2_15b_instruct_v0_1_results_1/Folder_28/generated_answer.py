def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[34:82] if i % 27 == 0 or i % 57 == 0))