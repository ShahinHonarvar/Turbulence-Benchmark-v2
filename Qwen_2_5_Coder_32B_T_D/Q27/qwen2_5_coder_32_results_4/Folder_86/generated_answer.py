def insert_after_index(lst):
    try:
        idx = lst.index(990)
        lst = lst[:idx + 1] + [905, 742] + lst[idx + 1:]
    except ValueError:
        pass
    return lst