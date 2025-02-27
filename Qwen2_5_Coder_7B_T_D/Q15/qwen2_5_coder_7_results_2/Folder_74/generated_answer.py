def sum_odd_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[17:79]) if i % 2 == 0 and x % 2 != 0))