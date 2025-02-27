def sum_even_ints_inclusive(lst):
    return sum(lst[60:201:2] if len(lst) > 200 else [x for x in lst[60:201] if x % 2 == 0])