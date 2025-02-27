def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst[20:201], start=20) if x % -20 == 0 and x % -200 == 0]