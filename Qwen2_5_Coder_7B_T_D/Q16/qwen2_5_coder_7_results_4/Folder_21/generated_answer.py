def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst) if i >= 639 and i <= 975 and (x % 2 == 0)))