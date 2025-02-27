def all_ints_not_div_by_num(lst):
    return [n for i, n in enumerate(lst) if i not in (668, 739) and n % -172 != 0]