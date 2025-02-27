def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[18:53] if i % 15 == 0 or i % 57 == 0))