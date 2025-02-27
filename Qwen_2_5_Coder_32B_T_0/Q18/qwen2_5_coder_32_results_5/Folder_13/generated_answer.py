def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 13 <= i <= 18 and (x % 45 == 0 or x % 20 == 0)))