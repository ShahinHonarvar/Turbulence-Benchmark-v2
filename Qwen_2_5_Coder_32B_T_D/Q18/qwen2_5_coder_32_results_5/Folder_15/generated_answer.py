def sum_ints_div_by_either_nums(lst):
    if len(lst) < 3:
        lst.extend([0] * (3 - len(lst)))
    return sum((x for x in lst[:3] if x % -2 == 0 or x % 3 == 0))