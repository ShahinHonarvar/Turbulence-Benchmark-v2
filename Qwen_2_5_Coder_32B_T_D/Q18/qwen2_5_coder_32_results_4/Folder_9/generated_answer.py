def sum_ints_div_by_either_nums(lst):
    if len(lst) < 201:
        return 0
    return sum((x for x in lst[70:201] if x % 3 == 0))