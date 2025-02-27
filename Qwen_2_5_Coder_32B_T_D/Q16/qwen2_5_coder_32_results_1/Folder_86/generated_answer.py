def sum_even_ints_inclusive(lst):
    return sum((x for x in lst[31:35] if x % 2 == 0)) if len(lst) > 34 else 0