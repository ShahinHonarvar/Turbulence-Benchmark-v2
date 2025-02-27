def insert_after_index(lst):
    index = lst.index(74)
    return lst[:index + 1] + [49] + lst[index + 1:]