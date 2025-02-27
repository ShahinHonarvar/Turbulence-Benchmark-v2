def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[20:201]) if i % 20 == 0 or i % 200 == 0))