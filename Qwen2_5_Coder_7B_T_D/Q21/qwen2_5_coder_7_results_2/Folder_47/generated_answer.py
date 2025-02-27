def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst, start=75) if i <= 88 and x % -27 == 0]