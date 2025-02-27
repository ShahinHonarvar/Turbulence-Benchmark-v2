def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 13 <= i <= 91 and x % -65 == 0 and (x % -62 == 0)]