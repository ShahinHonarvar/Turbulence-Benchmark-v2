def sum_odd_ints_inclusive(lst):
    if len(lst) < 606:
        return 0
    return sum((x for x in lst[533:606] if x % 2 != 0))