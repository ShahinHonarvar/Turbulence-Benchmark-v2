def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[50:201]) if i % 2 == 0 and (x % -34 == 0 or x % 64 == 0)))