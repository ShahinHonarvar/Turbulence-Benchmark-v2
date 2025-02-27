def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if 21 <= i <= 97 and x % 2 == 0))