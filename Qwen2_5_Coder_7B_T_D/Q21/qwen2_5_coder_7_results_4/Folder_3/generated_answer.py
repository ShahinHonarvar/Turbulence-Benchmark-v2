def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 25 and i <= 59 and (x % -26 == 0)]