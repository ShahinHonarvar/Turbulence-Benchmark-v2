def sum_ints_div_by_either_nums(ints):
    return sum((int for int in ints[72:94] if int % 32 == 0 or int % 44 == 0))