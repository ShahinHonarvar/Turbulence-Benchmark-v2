def all_ints_div_by_both_two_nums(lst):
    return [x for x in lst[:4] if x % 11 == 0 and x % -7 == 0]