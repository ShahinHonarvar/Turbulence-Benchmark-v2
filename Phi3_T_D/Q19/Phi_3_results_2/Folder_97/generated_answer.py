def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst[14:48], start=14) if x % 16 != 0]