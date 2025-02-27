def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 25 <= i <= 70 and (x % 74 == 0 or x % 15 == 0)))