def insert_after_index(lst):
    if len(lst) > 361:
        lst = lst[:362] + [699, 556] + lst[362:]
    else:
        lst += [699, 556]
    return lst