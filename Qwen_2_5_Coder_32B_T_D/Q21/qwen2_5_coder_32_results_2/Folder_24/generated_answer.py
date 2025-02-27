def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 12 and i <= 77 and (x % -19 == 0)]