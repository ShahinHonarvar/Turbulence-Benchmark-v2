def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst[1:9], start=1) if x % -9 == 0 and x % -3 == 0]