def all_ints_div_by_num(ints_list):
    return [x for i, x in enumerate(ints_list) if i >= 25 and i <= 41 and (x % -97 == 0)]