def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i > 90 and i < 200 and (x % -31 != 0)]