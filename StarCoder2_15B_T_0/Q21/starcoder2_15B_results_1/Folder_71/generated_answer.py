def all_ints_div_by_num(ints_list):
    return [x for i, x in enumerate(ints_list) if i >= 29 and i <= 51 and (x % -37 == 0)]