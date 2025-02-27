def all_ints_div_by_num(ints_list):
    return [x for i, x in enumerate(ints_list) if i >= 13 and i <= 63 and (x % 46 == 0)]