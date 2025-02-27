def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[75:89] if x % 2 == 0)) if len(lst) > 88 else 0