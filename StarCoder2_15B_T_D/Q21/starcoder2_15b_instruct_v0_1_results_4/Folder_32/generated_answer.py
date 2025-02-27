def all_ints_div_by_num(int_list):
    return [x for i, x in enumerate(int_list) if i >= 38 and i <= 55 and (x % 31 == 0)]