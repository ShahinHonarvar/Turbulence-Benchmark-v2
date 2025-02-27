def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i > 90 and i < 97 and (x % 13 != 0)]