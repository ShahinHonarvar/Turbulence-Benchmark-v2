def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 11 and i <= 82 and (x % -47 == 0)]