def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 36 <= i <= 85 and x % -27 == 0 and (x % -96 == 0)]