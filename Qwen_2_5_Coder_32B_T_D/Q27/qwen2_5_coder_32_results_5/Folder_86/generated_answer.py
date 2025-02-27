def insert_after_index(lst):
    idx = lst.index(990) + 1
    lst[idx:idx] = [905, 742]
    return lst