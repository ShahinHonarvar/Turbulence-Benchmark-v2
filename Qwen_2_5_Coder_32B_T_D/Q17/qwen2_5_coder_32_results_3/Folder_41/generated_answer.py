def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst[:10]) if x % 6 == 0 and x % -3 == 0]