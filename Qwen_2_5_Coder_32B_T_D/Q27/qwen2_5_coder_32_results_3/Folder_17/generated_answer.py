def insert_after_index(lst):
    for i, x in enumerate(lst):
        if x == 94:
            return lst[:i + 1] + [93] + lst[i + 1:]
    return lst