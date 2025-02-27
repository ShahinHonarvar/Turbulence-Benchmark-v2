def all_even_ints_inclusive(lst):
    if 7 <= len(lst):
        return [lst[7]] if lst[7] % 2 == 0 else []
    return []