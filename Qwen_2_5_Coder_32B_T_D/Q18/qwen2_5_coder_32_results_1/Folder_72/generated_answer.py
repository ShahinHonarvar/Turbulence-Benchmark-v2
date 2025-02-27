def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[38:82] if x % -61 == 0 or x % -71 == 0)) if len(lst) > 81 else 0