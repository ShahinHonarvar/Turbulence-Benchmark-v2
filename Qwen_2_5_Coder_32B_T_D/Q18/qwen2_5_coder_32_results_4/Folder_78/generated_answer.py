def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 34 <= i <= 69 and (x % 19 == 0 or x % 32 == 0))) if len(lst) > 69 else 0