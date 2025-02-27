def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 13 <= i <= 68 and x % 71 == 0]