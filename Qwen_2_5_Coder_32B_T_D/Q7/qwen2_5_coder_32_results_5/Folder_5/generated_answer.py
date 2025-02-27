def all_even_ints_inclusive(lst):
    if len(lst) < 10:
        return []
    return [x for x in lst[8:10] if x % 2 == 0]