def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i > 43 and i < 77 and (x % 84 != 0)]