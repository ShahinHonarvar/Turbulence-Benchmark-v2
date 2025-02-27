def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 86 <= i <= 90 and (x % -71 == 0 or x % -67 == 0))) if len(lst) > 90 else 0