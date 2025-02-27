def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 10 <= i <= 37 and x % -64 == 0]