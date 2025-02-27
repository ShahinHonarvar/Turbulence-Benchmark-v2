def sum_ints_div_by_either_nums(int_list):
    return sum((int_value for int_value in int_list[8:10] if int_value % -3 == 0 or int_value % 6 == 0))