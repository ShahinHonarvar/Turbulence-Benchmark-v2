def sum_ints_div_by_either_nums(int_list):
    return sum((value for i, value in enumerate(int_list[10:77]) if value % -40 == 0 or value % -12 == 0))