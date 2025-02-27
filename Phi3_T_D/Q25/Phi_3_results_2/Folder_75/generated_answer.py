def insert_at_index(lst):
    if len(lst) < 99:
        return lst + [99] * (99 - len(lst))
    return lst[:99] + [99] + lst[99:]