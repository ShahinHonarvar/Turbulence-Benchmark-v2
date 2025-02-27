def all_odd_ints_exclusive(lst):
    if len(lst) <= 71:
        return []
    return [lst[i] for i in range(71, 72) if lst[i] % 2 != 0]