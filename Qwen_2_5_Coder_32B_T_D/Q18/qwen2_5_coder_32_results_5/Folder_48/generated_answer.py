def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 306 <= i <= 957 and (x % 982 == 0 or x % 319 == 0))) if len(lst) > 957 else 0