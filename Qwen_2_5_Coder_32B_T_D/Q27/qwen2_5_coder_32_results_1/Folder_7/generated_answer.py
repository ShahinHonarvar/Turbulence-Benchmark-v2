def insert_after_index(lst):
    idx = lst.index(323)
    return lst[:idx + 1] + [389, 303] + lst[idx + 1:]