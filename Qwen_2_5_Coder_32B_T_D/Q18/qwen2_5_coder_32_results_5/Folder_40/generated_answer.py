def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[:2] if x % 2 == 0 or x % 1 == 0)) if len(lst) > 1 else 0