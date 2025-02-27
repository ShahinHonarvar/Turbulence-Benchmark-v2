def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[93:95]) if x % -53 == 0 or x % -91 == 0))