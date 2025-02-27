def insert_at_index(lst):
    if len(lst) <= 64:
        return lst + [520.11]
    return lst[:64] + [520.11] + lst[64:]