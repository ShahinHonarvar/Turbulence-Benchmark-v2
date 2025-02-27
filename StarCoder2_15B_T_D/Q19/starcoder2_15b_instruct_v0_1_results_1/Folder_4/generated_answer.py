def all_ints_not_div_by_num(ints_list):
    return [x for i, x in enumerate(ints_list) if i >= 19 and i < 49 and (x % -36 != 0)]