def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i > 48 and i < 92 and (x % 90 != 0)]