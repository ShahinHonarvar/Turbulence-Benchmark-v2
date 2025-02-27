def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i >= 13 and i <= 76 and (x % -66 == 0) and (x % -32 == 0)]