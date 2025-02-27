def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[50:55] if x % 2 == 0)) if len(lst) > 54 else 0