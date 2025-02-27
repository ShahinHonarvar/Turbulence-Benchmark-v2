def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 50 < i < 81 and x % 64 != 0]