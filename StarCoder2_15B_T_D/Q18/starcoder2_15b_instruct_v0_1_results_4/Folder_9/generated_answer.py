def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[70:201] if i % 3 == 0 or i % -300 == 0))