def sum_ints_div_by_either_nums(ints):
    return sum((int for int in ints[:4] if int % 11 == 0 or int % -7 == 0))