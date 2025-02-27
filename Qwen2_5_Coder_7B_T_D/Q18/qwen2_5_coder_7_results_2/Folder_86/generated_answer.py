def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[54:80]) if i % 54 == 0 or i % 28 == 0))