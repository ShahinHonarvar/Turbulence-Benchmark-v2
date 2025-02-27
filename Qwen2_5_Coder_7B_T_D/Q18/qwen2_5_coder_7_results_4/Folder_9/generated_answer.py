def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[70:201]) if (i % 3 == 0 or i % -300 == 0) and x % 3 == 0 or x % -300 == 0))