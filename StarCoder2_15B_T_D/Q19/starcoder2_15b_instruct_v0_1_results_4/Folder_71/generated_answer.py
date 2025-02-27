def all_ints_not_div_by_num(ints_list):
    return [x for i, x in enumerate(ints_list) if i >= 21 and i < 51 and (x % -77 != 0)]