def sum_odd_ints_inclusive(lst):
    total = sum((i for i in lst[19:93] if i % 2 != 0))
    return total