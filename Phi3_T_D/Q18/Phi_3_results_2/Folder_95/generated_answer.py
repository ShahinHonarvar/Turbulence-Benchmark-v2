def sum_ints_div_by_either_nums(int_list):
    sum_divisible = sum((value for index, value in enumerate(int_list[57:85]) if value % -30 == 0 or value % -88 == 0))
    return sum_divisible