def all_ints_not_div_by_num(ints_list):
    return [x for i, x in enumerate(ints_list) if i >= 20 and i < 200 and (x % -200 != 0)]