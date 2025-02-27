def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 10 <= i <= 28 and x % -61 == 0 and (x % -64 == 0)]