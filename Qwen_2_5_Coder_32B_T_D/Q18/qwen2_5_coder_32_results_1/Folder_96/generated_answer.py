def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 50 <= i <= 200 and (x % -34 == 0 or x % 64 == 0))) if len(lst) > 200 else 0