def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if i >= 20 and i <= 200 and (x % -20 == 0 or x % -200 == 0)))