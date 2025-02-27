def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 13 <= i <= 91 and (x % -65 == 0 or x % -62 == 0))) if len(lst) > 91 else 0