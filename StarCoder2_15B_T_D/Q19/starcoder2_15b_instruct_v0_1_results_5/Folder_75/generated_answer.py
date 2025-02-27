def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 20 and i < 51 and (x % -48 != 0)]