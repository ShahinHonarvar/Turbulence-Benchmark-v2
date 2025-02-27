def all_ints_div_by_both_two_nums(lst):
    return lst[0:1] if lst and lst[0] % 1 == 0 and (lst[0] % -1 == 0) else []