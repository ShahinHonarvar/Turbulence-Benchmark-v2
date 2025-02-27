def all_ints_not_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if 30 < i < 200 and num % -115 != 0]