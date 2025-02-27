def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 77 <= i <= 87 and (x % 23 == 0 or x % 57 == 0)))