def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 38 <= i <= 81 and x % -61 == 0 and (x % -71 == 0)]