def sum_ints_div_by_either_nums(int_list):
    total = sum((val for idx, val in enumerate(int_list[10:47], start=10) if val % 55 == 0 or val % 36 == 0))
    return total