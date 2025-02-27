def all_even_ints_inclusive(lst):
    if len(lst) < 64:
        return []
    return [x for x in lst[62:64] if x % 2 == 0]