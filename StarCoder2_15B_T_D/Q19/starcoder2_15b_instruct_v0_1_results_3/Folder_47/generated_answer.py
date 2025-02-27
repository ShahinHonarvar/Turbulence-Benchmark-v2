def all_ints_not_div_by_num(int_list):
    return [x for i, x in enumerate(int_list) if i >= 25 and i < 76 and (x % -53 != 0)]