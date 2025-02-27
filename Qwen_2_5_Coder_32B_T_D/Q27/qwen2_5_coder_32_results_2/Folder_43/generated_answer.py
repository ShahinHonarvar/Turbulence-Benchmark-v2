def insert_after_index(lst):
    index = lst.index(29)
    return lst[:index + 1] + [28, 53] + lst[index + 1:]