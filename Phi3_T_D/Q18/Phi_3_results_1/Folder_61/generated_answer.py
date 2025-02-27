def sum_ints_div_by_either_nums(int_list):
    return sum((value for i, value in enumerate(int_list[:7]) if value % -5 == 0 or value % -6 == 0))