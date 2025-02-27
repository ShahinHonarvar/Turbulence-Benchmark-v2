def sum_ints_div_by_either_nums(ints):
    return sum((i for i in ints[80:201] if i % 10 == 0 or i % 1000 == 0))