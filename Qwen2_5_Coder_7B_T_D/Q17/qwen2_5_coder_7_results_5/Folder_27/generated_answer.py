def all_ints_div_by_both_two_nums(lst):
    return [x for i, x in enumerate(lst) if i >= 20 and i <= 35 and (x % -36 == 0) and (x % -89 == 0)]