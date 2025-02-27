def sum_ints_div_by_either_nums(lst):
    if len(lst) < 201:
        return 0
    return sum((x for i, x in enumerate(lst[80:201]) if x % 10 == 0 or x % 1000 == 0))