def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 22 <= i <= 63 and x % -61 == 0]