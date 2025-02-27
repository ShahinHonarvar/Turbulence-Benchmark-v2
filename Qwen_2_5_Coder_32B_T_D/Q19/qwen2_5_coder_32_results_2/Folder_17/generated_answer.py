def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if not 39 < i < 57 or (39 < i < 57 and x % 84 != 0)]