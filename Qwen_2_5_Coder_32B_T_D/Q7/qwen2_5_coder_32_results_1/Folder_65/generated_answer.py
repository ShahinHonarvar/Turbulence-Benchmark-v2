def all_even_ints_inclusive(lst):
    if len(lst) < 99:
        return []
    return [x for x in lst[56:99] if x % 2 == 0]