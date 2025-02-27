def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 10 <= i <= 52 and x % -12 == 0]