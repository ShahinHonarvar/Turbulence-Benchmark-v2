def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst[34:82], start=34) if x % 27 == 0 and x % 57 == 0]