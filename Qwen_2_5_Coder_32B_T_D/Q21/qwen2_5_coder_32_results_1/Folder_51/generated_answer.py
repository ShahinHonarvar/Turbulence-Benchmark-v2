def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 5 and i <= 6 and (x % -6 == 0)]