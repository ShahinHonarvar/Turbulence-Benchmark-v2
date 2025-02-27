def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[40:42] if x % 2 == 0)) if len(lst) > 41 else 0