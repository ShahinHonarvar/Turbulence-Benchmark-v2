def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 81 <= i <= 86 and (x % -33 == 0 or x % -62 == 0))) if len(lst) > 86 else 0