def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst[81:90]) if x % 56 == 0 and x % 68 == 0]