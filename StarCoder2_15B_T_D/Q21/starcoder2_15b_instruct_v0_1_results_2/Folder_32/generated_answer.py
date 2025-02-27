def all_ints_div_by_num(ints_list):
    return [x for i, x in enumerate(ints_list) if i >= 38 and i <= 55 and (x % 31 == 0)]