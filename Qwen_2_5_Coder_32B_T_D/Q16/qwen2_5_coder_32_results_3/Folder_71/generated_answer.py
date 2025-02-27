def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[26:53] if x % 2 == 0)) if len(lst) > 52 else sum((x for x in lst[26:] if x % 2 == 0))