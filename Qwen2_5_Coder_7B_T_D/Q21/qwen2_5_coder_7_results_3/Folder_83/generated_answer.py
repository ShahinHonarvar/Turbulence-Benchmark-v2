def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 40 and i <= 400 and (x % 7 == 0)]