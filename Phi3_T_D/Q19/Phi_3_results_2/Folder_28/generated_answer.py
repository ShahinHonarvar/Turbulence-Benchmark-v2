def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst[81:86], start=81) if x % 77 != 0]