def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 59 and i <= 97 and (x % -36 == 0)]