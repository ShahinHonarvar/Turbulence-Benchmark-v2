def insert_after_index(lst):
    if len(lst) <= 51:
        raise IndexError('Index 52 does not exist')
    return lst[:52] + [304.62] + lst[52:]