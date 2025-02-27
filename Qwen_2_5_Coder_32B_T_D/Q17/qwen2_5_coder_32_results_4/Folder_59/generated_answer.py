def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i <= 8 and x % -3 == 0 and (x % 8 == 0)]