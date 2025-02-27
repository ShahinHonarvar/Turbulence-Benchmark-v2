def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst[:11]) if i <= 10 and x % 2 == 0]