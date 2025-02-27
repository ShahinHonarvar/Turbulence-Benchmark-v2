def sum_ints_div_by_either_nums(int_list):
    return sum((n for i, n in enumerate(int_list[20:36], start=20) if n % -36 == 0 or n % -89 == 0))