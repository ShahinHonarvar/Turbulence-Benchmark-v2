def all_ints_not_div_by_num(int_list):
    return [x for i, x in enumerate(int_list) if 18 < i < 60 and x % 86 != 0]