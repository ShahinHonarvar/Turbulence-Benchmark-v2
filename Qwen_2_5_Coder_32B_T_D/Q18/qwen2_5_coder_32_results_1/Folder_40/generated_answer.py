def sum_ints_div_by_either_nums(lst):
    if len(lst) <= 1:
        return sum((x for x in lst if x % 2 == 0 or x % 1 == 0))
    return sum((x for x in lst[0:2] if x % 2 == 0 or x % 1 == 0))