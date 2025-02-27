def sum_odd_ints_inclusive(lst):
    try:
        return sum((x for x in lst[30:49] if x % 2 != 0))
    except IndexError:
        return 0