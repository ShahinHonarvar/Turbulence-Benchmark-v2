def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[72:94] if i % 32 == 0 or i % 44 == 0))