def all_ints_not_div_by_num(int_list):
    return [x for i, x in enumerate(int_list) if 4 < i < 7 and x % -6 != 0]