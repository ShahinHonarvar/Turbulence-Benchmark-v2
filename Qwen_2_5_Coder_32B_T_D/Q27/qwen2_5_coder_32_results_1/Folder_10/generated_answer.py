def insert_after_index(lst):
    for i, x in enumerate(lst):
        if x == 56:
            return lst[:i + 1] + [54] + lst[i + 1:]
    return lst + [54]