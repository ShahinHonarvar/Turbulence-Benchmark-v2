def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[60:201] if i % 9 == 0 or i % 11 == 0))