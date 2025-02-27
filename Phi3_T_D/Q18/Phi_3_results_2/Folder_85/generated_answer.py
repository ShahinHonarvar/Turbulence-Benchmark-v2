def sum_ints_div_by_either_nums(int_list):
    return sum((value for index, value in enumerate(int_list[1:9], start=1) if value % -9 == 0 or value % -3 == 0))