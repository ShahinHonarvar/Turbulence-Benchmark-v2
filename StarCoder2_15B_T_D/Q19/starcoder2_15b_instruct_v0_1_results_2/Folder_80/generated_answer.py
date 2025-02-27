def all_ints_not_div_by_num(int_list):
    return [x for i, x in enumerate(int_list) if i >= 15 and i < 20 and (x % 93 != 0)]