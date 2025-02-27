def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst[:6]) if i <= 5 and x % 2 == 0]