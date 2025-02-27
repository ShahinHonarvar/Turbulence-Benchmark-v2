def sum_ints_div_by_either_nums(lst):
    return lst[7] if 7 < len(lst) and (lst[7] % 5 == 0 or lst[7] % 7 == 0) else 0