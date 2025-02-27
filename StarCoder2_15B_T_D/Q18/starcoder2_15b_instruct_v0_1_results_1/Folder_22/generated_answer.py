def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[40:201] if i % 21 == 0 or i % 71 == 0))