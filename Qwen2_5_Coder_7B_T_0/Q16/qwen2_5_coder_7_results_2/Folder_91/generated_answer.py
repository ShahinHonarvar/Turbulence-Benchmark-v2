def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[:6]) if i <= 5 and x % 2 == 0))