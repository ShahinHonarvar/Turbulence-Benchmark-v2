def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i >= 7 and i <= 9 and (x % -9 == 0) and (x % -7 == 0)]