def all_ints_div_by_num(int_list):
    return [x for i, x in enumerate(int_list) if i >= 27 and i <= 90 and (x % 57 == 0)]