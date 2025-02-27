def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if 20 <= i <= 93 and x % -92 == 0 and (x % -50 == 0)]