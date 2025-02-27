def all_ints_div_by_num(ints_list):
    return [x for i, x in enumerate(ints_list) if i >= 22 and i <= 63 and (x % -61 == 0)]