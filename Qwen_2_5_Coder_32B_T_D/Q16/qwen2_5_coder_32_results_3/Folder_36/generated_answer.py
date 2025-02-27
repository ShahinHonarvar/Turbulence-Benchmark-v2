def sum_even_ints_inclusive(lst):
    if len(lst) < 751:
        return 0
    return sum((x for x in lst[246:751] if x % 2 == 0))