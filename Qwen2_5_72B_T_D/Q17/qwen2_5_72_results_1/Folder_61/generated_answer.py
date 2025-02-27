def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst[:7]) if x % -5 == 0 and x % -6 == 0]