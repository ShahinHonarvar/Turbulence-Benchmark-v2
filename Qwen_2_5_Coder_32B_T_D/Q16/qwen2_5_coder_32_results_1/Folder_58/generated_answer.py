def sum_even_ints_inclusive(lst):
    if len(lst) < 557:
        return 0
    return sum((x for x in lst[209:557] if x % 2 == 0))