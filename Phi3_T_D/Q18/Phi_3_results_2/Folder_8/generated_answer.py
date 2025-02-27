def sum_ints_div_by_either_nums(int_list):
    return sum((value for index, value in enumerate(int_list[36:86], start=36) if value % -27 == 0 or value % -96 == 0))