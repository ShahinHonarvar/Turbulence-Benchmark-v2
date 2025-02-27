def all_ints_not_div_by_num(int_list):
    return [x for i, x in enumerate(int_list) if i >= 24 and i < 45 and (x % -72 != 0)]