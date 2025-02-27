def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 41 <= i <= 56 and (x % 82 == 0 or x % 90 == 0))) if len(lst) > 56 else 0