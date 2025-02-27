def insert_after_index(lst):
    for i, x in enumerate(lst):
        if x == 90:
            return lst[:i + 1] + [80] + lst[i + 1:]
    return lst