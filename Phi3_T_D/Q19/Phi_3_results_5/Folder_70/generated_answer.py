def all_ints_not_div_by_num(lst):
    return [x for i, x in enumerate(lst[90:97]) if i + 90 not in (i + 90 for i in range(0, 16, 13)) and x % 13 != 0]