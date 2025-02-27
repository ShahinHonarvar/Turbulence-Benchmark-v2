def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[5:7] if i % 22 == 0 or i % 82 == 0))