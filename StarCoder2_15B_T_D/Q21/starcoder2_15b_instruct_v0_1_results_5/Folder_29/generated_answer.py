def all_ints_div_by_num(ints_list):
    return [x for i, x in enumerate(ints_list) if i >= 52 and i <= 72 and (x % -15 == 0)]