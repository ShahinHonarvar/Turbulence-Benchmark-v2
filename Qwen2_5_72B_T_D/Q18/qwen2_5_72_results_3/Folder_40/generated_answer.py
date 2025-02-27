def sum_ints_div_by_either_nums(lst):
    if len(lst) < 2:
        return 0
    subset = lst[0:2]
    return sum([x for x in subset if x % 2 == 0 or x % 1 == 0])