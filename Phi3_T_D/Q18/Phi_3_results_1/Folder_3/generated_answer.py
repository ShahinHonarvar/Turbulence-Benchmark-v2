def sum_ints_div_by_either_nums(int_list):
    return sum((val for i, val in enumerate(int_list[38:53], start=38) if val % -41 == 0 or val % -47 == 0))