def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if i >= 828 and i <= 932 and (x % -649 == 0 or x % -461 == 0)))