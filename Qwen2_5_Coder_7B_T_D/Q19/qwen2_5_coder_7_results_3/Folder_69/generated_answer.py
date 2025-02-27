def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i > 45 and i < 72 and (x % 93 != 0)]