def sum_even_ints_inclusive(lst):
    if len(lst) <= 746:
        return 0
    return sum((x for x in lst[262:747] if x % 2 == 0))