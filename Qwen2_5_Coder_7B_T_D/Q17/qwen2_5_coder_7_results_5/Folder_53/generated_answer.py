def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i >= 200 and i <= 200 and (x % 17 == 0) and (x % -5 == 0)]