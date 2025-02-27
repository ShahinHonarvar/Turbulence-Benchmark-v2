def insert_after_index(lst):
    for i, x in enumerate(lst):
        if x == 44:
            return lst[:i + 1] + [76] + lst[i + 1:]
    return lst