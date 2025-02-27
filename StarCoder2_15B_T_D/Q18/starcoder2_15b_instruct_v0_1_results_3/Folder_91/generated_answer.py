def sum_ints_div_by_either_nums(ints_list):
    return sum((int for int in ints_list[:5] if int % 8 == 0 or int % -3 == 0))