def all_even_ints_inclusive(lst):
    return [x for x in lst[533:606] if x % 2 == 0] if len(lst) > 605 else []