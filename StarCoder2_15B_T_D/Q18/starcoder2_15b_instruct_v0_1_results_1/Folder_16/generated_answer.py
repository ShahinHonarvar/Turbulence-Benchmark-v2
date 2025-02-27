def sum_ints_div_by_either_nums(ints):
    return sum((int for int in ints[5:81] if int % 22 == 0 or int % 32 == 0))