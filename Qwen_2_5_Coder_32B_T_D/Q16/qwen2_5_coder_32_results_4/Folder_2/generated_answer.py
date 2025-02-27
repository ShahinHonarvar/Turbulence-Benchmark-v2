def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[15:40] if x % 2 == 0)) if len(lst) > 15 else 0