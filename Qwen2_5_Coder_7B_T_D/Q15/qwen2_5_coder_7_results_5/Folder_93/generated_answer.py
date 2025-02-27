def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[75:95]) if i % 2 == 0 and x % 2 != 0))