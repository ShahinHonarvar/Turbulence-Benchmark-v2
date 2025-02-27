def insert_after_index(lst):
    for i, x in enumerate(lst):
        if x == 99:
            return lst[:i + 1] + [99] + lst[i + 1:]
    return lst