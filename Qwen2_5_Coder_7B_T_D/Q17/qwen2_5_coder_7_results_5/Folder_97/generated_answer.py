def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst[58:76]) if x % 72 == 0 and x % 62 == 0]