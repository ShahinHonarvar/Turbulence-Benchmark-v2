def all_even_ints_inclusive(lst):
    if len(lst) < 201:
        return []
    return [x for x in lst[40:201] if x % 2 == 0]