def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 90 <= i <= 200 and (x % -31 == 0 or x % 13 == 0))) if len(lst) > 90 else 0