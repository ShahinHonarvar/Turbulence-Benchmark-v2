def all_even_ints_inclusive(lst):
    return lst[0:2] if 0 < len(lst) else [] if any((x % 2 == 0 for x in lst[0:2])) else []