def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 18 <= i <= 52 and (x % 15 == 0 or x % 57 == 0)))