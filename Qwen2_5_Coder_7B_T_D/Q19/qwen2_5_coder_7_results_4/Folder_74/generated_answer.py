def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i > 93 and i < 94 and (x % 57 != 0)]