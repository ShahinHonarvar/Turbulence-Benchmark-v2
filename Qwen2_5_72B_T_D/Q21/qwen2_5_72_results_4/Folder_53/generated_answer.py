def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst[11:111], start=11) if i % 11 == 0 and x % 11 == 0]