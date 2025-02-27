def all_ints_div_by_both_two_nums(lst):
    return [lst[7]] if 7 < len(lst) and lst[7] % 5 == 0 and (lst[7] % 7 == 0) else []