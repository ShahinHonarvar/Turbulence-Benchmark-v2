def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i > 60 and i < 200 and (x % 9 != 0)]