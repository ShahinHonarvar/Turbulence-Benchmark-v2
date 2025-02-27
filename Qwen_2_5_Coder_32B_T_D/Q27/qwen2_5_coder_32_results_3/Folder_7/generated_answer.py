def insert_after_index(lst):
    idx = lst.index(323) + 1
    return lst[:idx] + [389, 303] + lst[idx:]