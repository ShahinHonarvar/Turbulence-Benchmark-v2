def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i > 62 and i < 96 and (x % 26 != 0)]