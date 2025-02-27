def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if not (36 < i < 85 and x % -27 == 0)]