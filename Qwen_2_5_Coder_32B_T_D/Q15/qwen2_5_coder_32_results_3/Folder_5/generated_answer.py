def sum_odd_ints_inclusive(lst):
    if len(lst) < 10:
        return 0
    return sum((x for x in lst[8:10] if x % 2 == 1))