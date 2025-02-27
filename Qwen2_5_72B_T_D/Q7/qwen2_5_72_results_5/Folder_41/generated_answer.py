def all_even_ints_inclusive(lst):
    if 6 < 0 or 6 >= len(lst):
        return []
    return [lst[6]] if lst[6] % 2 == 0 else []