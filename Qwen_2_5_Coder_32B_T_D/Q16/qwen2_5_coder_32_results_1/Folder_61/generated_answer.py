def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[:8] if x % 2 == 0)) if len(lst) > 7 else sum((x for x in lst if x % 2 == 0))