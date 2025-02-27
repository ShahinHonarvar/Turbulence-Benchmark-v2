def sum_even_ints_inclusive(lst):
    if 41 < len(lst):
        return sum((x for x in lst[40:42] if x % 2 == 0))
    return 0