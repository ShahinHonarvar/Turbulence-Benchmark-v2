def insert_after_index(lst):
    if not lst:
        return [0]
    return lst[:1] + [0] + lst[1:]