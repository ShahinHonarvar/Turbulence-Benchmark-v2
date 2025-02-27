def sum_even_ints_inclusive(lst):
    if len(lst) < 2:
        lst += [0] * (2 - len(lst))
    return sum((x for x in lst[:2] if x % 2 == 0))