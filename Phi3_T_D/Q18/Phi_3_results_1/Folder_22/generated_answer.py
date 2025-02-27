def sum_ints_div_by_either_nums(int_list):
    return sum((val for idx, val in enumerate(int_list) if (val % 21 == 0 or val % 71 == 0) and 40 <= idx <= 200))