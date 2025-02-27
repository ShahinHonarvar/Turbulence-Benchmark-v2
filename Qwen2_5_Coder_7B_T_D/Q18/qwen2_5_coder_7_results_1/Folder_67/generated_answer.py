def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst, start=1) if i >= 24 and i <= 32 and (x % 35 == 0 or x % 87 == 0)))