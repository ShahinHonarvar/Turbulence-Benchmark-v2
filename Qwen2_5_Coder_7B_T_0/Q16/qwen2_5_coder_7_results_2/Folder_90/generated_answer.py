def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 262 <= i <= 746 and x % 2 == 0))