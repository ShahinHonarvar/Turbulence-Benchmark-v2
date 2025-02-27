def all_even_ints_inclusive(lst):
    return [x for i, x in enumerate(lst[1:9], start=2) if x % 2 == 0]