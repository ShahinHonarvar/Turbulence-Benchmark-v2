def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i > 0 and i < 5 and (x % 8 != 0)]