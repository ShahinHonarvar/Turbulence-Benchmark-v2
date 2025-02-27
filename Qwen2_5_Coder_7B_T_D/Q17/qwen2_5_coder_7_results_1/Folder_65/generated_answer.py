def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst[50:93]) if x % -94 == 0 and x % -95 == 0]