def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i > 84 and i < 86 and (x % 99 != 0)]