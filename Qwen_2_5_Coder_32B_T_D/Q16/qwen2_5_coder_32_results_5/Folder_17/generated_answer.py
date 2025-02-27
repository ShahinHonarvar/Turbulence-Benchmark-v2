def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[62:79] if x % 2 == 0)) if len(lst) > 78 else 0