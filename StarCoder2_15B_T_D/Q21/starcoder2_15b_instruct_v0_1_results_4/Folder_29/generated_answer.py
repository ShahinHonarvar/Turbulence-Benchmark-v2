def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 52 and i <= 72 and (x % -15 == 0)]