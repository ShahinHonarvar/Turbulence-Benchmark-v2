def sum_ints_div_by_either_nums(lst):
    if len(lst) < 95:
        return 0
    return lst[93] + lst[94] if (lst[93] % -53 == 0 or lst[93] % -91 == 0) and (lst[94] % -53 == 0 or lst[94] % -91 == 0) else 0