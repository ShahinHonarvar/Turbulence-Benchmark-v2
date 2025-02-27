def all_ints_div_by_num(int_list):
    return [x for i, x in enumerate(int_list) if i >= 13 and i <= 68 and (x % 71 == 0)]