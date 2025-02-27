def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[1:9] if x % 2 == 0)) if len(lst) > 8 else sum((x for x in lst[1:] if x % 2 == 0))