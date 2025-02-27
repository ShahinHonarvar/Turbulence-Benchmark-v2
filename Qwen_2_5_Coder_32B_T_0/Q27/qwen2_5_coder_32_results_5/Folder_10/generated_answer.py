def insert_after_index(lst):
    for i in range(len(lst)):
        if lst[i] == 56:
            return lst[:i + 1] + [54] + lst[i + 1:]
    return lst