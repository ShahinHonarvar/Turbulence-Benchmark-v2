def all_even_ints_inclusive(lst):
    if len(lst) <= 73:
        return []
    return [lst[73]] if lst[73] % 2 == 0 else []