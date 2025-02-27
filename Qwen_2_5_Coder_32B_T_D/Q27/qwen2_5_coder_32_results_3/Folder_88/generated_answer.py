def insert_after_index(lst):
    index_91 = lst.index(91)
    return lst[:index_91 + 1] + [46, 13] + lst[index_91 + 1:]