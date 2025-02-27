def all_ints_div_by_num(ints_list):
    return [x for i, x in enumerate(ints_list) if i >= 12 and i <= 77 and (x % -19 == 0)]