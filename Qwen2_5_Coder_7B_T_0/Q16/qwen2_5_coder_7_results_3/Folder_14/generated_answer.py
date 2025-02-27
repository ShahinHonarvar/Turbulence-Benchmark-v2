def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 5 <= i <= 7 and x % 2 == 0))