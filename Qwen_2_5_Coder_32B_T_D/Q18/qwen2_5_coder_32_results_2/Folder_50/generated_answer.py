def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 46 <= i <= 91 and (x % 67 == 0 or x % 15 == 0))) if len(lst) > 91 else 0