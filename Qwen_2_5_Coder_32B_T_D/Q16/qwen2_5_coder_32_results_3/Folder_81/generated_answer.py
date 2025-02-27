def sum_even_ints_inclusive(lst):
    if len(lst) < 101:
        return 0
    return sum((x for x in lst[10:101] if x % 2 == 0))