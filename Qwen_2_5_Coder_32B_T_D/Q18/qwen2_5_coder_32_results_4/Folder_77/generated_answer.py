def sum_ints_div_by_either_nums(lst):
    if len(lst) < 933:
        return 0
    return sum((x for x in lst[828:933] if x % -649 == 0 or x % -461 == 0))