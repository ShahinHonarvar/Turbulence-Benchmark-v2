def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 35 and i < 98 and (x % 41 != 0)]