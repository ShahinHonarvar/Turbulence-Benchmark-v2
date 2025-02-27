def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i >= 55 and i <= 84 and (x % -24 == 0) and (x % -11 == 0)]