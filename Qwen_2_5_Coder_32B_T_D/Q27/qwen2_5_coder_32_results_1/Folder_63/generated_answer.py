def insert_after_index(lst):
    for i, x in enumerate(lst):
        if x == 76:
            return lst[:i + 1] + [15, 51] + lst[i + 1:]
    return lst