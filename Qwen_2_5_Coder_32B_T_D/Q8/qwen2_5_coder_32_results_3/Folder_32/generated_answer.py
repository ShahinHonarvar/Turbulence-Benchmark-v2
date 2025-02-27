def all_even_ints_exclusive(lst):
    if len(lst) <= 76:
        return []
    return [x for x in lst[12:76] if x % 2 == 0]