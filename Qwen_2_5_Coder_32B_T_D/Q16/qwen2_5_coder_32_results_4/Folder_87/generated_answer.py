def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[36:47] if x % 2 == 0)) if len(lst) > 46 else 0