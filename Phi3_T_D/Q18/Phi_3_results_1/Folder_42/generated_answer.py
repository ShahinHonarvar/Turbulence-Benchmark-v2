def sum_ints_div_by_either_nums(int_list):
    return sum((value for value in int_list[29:46] if value % 27 == 0 or value % 81 == 0))