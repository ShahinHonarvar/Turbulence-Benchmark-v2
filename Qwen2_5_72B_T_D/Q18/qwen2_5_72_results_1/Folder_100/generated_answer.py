def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[72:94] if x % 32 == 0 or x % 44 == 0)) if len(lst) > 93 else 0