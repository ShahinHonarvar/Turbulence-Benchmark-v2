def all_ints_not_div_by_num(int_list):
    return [num for i, num in enumerate(int_list) if 19 < i < 49 and num % -36 != 0]