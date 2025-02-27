def sum_odd_ints_inclusive(lst):
    if len(lst) < 201:
        return 0
    return sum((x for x in lst[60:201] if x % 2 != 0))