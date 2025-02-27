def all_even_ints_inclusive(lst):
    if len(lst) <= 7:
        return []
    return [lst[7]] if lst[7] % 2 == 0 else []