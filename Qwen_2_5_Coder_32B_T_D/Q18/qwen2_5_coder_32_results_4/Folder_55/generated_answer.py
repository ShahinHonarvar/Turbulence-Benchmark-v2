def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[:10]) if x % 10 == 0 or x % 100 == 0))