def insert_after_index(lst):
    index = lst.index(96)
    return lst[:index + 1] + [36] + lst[index + 1:]