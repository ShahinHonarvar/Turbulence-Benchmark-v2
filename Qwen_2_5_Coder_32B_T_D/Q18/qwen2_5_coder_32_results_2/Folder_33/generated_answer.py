def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 281 <= i <= 694 and (x % -722 == 0 or x % -731 == 0))) if len(lst) > 694 else 0