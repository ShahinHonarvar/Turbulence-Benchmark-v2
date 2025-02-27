def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[48:60] if x % 88 == 0 or x % 58 == 0)) if len(lst) > 59 else 0