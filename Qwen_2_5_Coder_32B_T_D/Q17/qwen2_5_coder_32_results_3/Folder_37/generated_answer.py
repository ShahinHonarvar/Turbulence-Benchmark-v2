def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 2 <= i <= 7 and x % -1 == 0 and (x % -7 == 0)]