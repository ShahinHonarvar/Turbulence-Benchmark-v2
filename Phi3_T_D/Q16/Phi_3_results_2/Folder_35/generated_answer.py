def sum_even_ints_inclusive(lst):
    return sum((val for idx, val in enumerate(lst[30:49]) if val % 2 == 0))