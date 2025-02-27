def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i >= 6 and i <= 9 and (x % -1 == 0) and (x % -10 == 0)]