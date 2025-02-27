def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 315 <= i <= 934 and (x % -897 == 0 or x % -556 == 0))) if len(lst) > 934 else 0