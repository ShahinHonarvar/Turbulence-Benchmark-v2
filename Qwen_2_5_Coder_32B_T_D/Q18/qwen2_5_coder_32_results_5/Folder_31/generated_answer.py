def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 56 <= i <= 88 and (x % -59 == 0 or x % -79 == 0))) if len(lst) > 88 else 0