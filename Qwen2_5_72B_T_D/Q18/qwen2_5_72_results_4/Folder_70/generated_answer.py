def sum_ints_div_by_either_nums(lst):
    if len(lst) < 44:
        return 0
    subset = lst[42:44]
    return sum((x for x in subset if x % 15 == 0 or x % 87 == 0))