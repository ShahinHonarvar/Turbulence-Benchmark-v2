def sum_ints_div_by_either_nums(int_list):
    return sum((int_list[0] % div == 0 for div in [-1, 1])) * int_list[0] if int_list else 0