def sum_ints_div_by_either_nums(ints):
    return sum((int for int in ints[50:201] if int % -34 == 0 or int % 64 == 0))