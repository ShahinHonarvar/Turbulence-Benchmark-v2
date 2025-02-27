def all_ints_not_div_by_num(int_list):
    return [x for i, x in enumerate(int_list) if i >= 4 and i < 5 and (x % -7 != 0)]