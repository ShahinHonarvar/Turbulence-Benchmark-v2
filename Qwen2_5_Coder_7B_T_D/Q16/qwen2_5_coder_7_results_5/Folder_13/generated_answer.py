def sum_even_ints_inclusive(lst):
    return sum((x for i, x in enumerate(lst[25:88]) if i % 2 == 0 and x % 2 == 0))