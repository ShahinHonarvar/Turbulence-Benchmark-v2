def all_even_ints_inclusive(lst):
    if len(lst) < 36:
        return []
    return [x for x in lst[32:36] if x % 2 == 0]