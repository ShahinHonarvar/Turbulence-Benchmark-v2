def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if 25 <= i <= 59 and x % -26 == 0]