def sum_ints_div_by_either_nums(int_list):
    return sum((int_val for int_val in int_list[:10] if int_val % 6 == 0 or int_val % -3 == 0))