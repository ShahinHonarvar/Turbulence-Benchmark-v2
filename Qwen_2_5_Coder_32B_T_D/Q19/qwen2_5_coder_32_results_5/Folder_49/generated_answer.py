def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 80 < i < 200 and x % 1000 != 0]