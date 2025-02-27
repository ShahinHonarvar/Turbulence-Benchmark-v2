def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst[29:52], start=29) if x % -68 != 0]