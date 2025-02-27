def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i >= 68 and i <= 99 and (x % -37 == 0) and (x % -26 == 0)]