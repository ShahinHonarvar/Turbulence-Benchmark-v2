def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[50:201] if x % 2 == 0)) if len(lst) > 200 else 0