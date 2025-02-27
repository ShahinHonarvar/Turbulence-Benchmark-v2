def sum_ints_div_by_either_nums(lst):
    if len(lst) > 1:
        return sum((x for x in lst[:2] if x % 2 == 0 or x % 1 == 0))
    elif len(lst) == 1:
        return lst[0] if lst[0] % 2 == 0 or lst[0] % 1 == 0 else 0
    return 0