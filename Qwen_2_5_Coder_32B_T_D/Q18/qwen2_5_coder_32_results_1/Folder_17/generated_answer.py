def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 81 <= i <= 89 and (x % 56 == 0 or x % 68 == 0))) if len(lst) > 89 else 0