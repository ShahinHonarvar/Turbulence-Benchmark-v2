def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 80 <= i <= 200 and (x % 10 == 0 or x % 1000 == 0)))