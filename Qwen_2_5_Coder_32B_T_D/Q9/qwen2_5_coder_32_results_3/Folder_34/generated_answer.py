def all_odd_ints_inclusive(lst):
    return [lst[i] for i in range(60, 61) if lst[i] % 2 != 0] if len(lst) > 60 else []