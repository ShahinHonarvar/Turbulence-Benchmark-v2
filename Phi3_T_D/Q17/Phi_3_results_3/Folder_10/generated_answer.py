def all_ints_div_by_both_two_nums(lst):
    return [x for x in lst[32:99 + 1] if x % -11 == 0 and x % -15 == 0]