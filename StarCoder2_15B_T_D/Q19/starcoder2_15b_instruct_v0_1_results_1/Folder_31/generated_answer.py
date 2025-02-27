def all_ints_not_div_by_num(int_list):
    return [x for i, x in enumerate(int_list) if i >= 18 and i < 37 and (x % -67 != 0)]