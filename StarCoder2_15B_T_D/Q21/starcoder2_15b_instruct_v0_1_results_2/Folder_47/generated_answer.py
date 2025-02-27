def all_ints_div_by_num(int_list):
    return [x for i, x in enumerate(int_list) if i >= 75 and i <= 88 and (x % -27 == 0)]