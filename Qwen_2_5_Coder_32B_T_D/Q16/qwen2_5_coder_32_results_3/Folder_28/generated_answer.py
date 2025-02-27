def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[62:64] if x % 2 == 0)) if len(lst) > 63 else 0