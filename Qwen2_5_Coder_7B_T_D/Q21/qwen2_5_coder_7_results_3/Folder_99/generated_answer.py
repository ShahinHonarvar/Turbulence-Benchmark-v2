def all_ints_div_by_num(lst):
    return [x for i, x in enumerate(lst) if i >= 161 and i <= 970 and (x % 763 == 0)]