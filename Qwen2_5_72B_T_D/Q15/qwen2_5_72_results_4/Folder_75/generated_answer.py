def sum_odd_ints_inclusive(lst):
    try:
        segment = lst[56:58]
        return sum((x for x in segment if x % 2 != 0))
    except IndexError:
        return 0