def sum_ints_div_by_either_nums(int_list):
    return sum((val for idx, val in enumerate(int_list[7:10]) if val % -9 == 0 or val % -7 == 0))