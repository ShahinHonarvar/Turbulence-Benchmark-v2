def all_ints_div_by_num(ints_list):
    return [x for i, x in enumerate(ints_list) if i >= 27 and i <= 86 and (x % 29 == 0)]