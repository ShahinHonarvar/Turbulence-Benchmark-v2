def insert_after_index(lst):
    index = lst.index(990)
    return lst[:index + 1] + [905, 742] + lst[index + 1:]