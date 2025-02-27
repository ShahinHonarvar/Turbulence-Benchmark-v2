def all_even_ints_exclusive(lst):
    if len(lst) > 94:
        return [x for x in lst[93:95] if x % 2 == 0]
    return []