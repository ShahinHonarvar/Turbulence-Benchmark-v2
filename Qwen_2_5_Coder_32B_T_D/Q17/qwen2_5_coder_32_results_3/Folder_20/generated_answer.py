def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 48 <= i <= 76 and x % -46 == 0 and (x % -82 == 0)]