def all_ints_not_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if 13 < i < 70 and num % -78 != 0]