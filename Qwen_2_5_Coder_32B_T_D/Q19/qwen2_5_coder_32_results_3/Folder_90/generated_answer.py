def all_ints_not_div_by_num(lst):
    if len(lst) <= 905:
        return []
    return [x for i, x in enumerate(lst) if i > 767 and i < 905 and (x % -430 != 0)]