def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[14:94] if i % 71 == 0 or i % 81 == 0))